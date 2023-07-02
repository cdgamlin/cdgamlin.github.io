import json
import re
import random
import urllib.request

with open('config.json', 'r') as rfile:
    config = json.load(rfile)

INPUT_FILE = config['INPUT_FILE']
OUTPUT_FILE = config['OUTPUT_FILE']
USER_AGENTS = config['USER_AGENTS']
EDIT_GROUP_TITLES = config['EDIT_GROUP_TITLES']
COUNTRY_TO_SUBCONTINENT_AND_CODE = config['COUNTRY_TO_SUBCONTINENT_AND_CODE']
EDIT_TITLES = config['EDIT_TITLES']

with open(INPUT_FILE, 'r') as rfile:
    sources = rfile.read().splitlines()

m3ulist = []
for url in sources:
    if url.startswith('#') or url=='':
        continue
    assert(url.startswith('http://') or url.startswith('https://'))
    response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(USER_AGENTS)}))
    download = response.read().decode('utf-8').split('\n')
    for x in range(len(download)):
        if download[x].startswith('#EXTINF:') and download[x+1].startswith('http'):
            m3ulist += [f'{download[x]}" link="{download[x+1]}"'.replace(',',' title="')]

m3ulist = [{key: value for key, value in re.compile(r'(\S+)="([^"]*)"').findall(x)} for x in m3ulist]
link_dct = {}
dct_list = []
for dct in m3ulist:
    if dct['link'] in link_dct:
        existing_dct = link_dct[dct['link']]
        for key, value in dct.items():
            if key not in existing_dct:
                existing_dct[key] = value
    else:
        dct_list.append(dct)
        link_dct[dct['link']] = dct
m3ulist = dct_list

domain=[x['link'].split('/')[2].split('.')[-2].upper() for x in m3ulist]
domain=[(x if not x.isdigit() else '')+'ZYZ' for x in domain]
domain=[(x[0] + ''.join([char for i, char in enumerate(x) if char not in 'AEIOU-' or i == 0 or i == len(x)-4][1:-4]) + x[-4:])[:4] for x in domain]

country_code = [x['link'].split('/')[2].split('.')[-1].split(':')[0] for x in m3ulist]
country_code = [x.upper() if len(x)==2 and not x.isdigit() else 'TV' for x in country_code]

group_title = [x['group-title'].split(';')[-1] if 'group-title' in x else 'XYZ' for x in m3ulist]
for key, value in EDIT_GROUP_TITLES.items():
    group_title = [x.replace(key,value) for x in group_title]
group_title = [x.lower() for x in group_title]

# 'NZ' needs to be treated as 'TV', as 'NZ' country code is problematic due to M3U lists from https://i.mjh.nz
country_code = [(COUNTRY_TO_SUBCONTINENT_AND_CODE.get(x[0],['','TV'])[1] if x[1] in ['TV','NZ'] else x[1]) for x in zip(group_title,country_code)]

group_title = [f"X:{COUNTRY_TO_SUBCONTINENT_AND_CODE[x][0]}" if x in COUNTRY_TO_SUBCONTINENT_AND_CODE else x for x in group_title]

m3ulist = [{**dct1, **dct2} for dct1, dct2 in zip(m3ulist, [{'domain':x.upper()} for x in domain])]
m3ulist = [{**dct1, **dct2} for dct1, dct2 in zip(m3ulist, [{'country-code':x.upper()} for x in country_code])]
m3ulist = [{**dct1, **dct2} for dct1, dct2 in zip(m3ulist, [{'group-title':x.upper()} for x in group_title])]

title = [f"{x['title']} [{x['domain']}:{x['country-code']}]".replace('#','').strip().upper() for x in m3ulist]
for key, value in EDIT_TITLES.items():
    title =[(x.replace(key.upper(), '', 1).strip()[:-10] + value + x[-10:] if x.startswith(key.upper()) else x) for x in title]
m3ulist = [{**dct1, **dct2} for dct1, dct2 in zip(m3ulist, [{'title':x.strip().upper()} for x in title])]

m3ulist = sorted(m3ulist, key=lambda x: x['title'].lower())
m3ulist = sorted(m3ulist, key=lambda x: x['group-title'].lower())

with open(OUTPUT_FILE, 'w') as wfile:
    wfile.write('#EXTM3U\n')
    tvg_chno = 1
    for entry in m3ulist:
        wfile.write(f'#EXTINF:-1 tvg-chno="{tvg_chno}" group-title="{entry["group-title"]}" tvg-logo="{entry["tvg-logo"]}",{entry["title"]}\n{entry["link"]}\n\n')
        tvg_chno += 1
