# [cdgamlin.github.io](https://github.com/cdgamlin/cdgamlin.github.io/)

# PARS: *Playlist Aggregator Refiner Scheme*

Parses multiple FREE online M3U playlists to generate a custom IPTV.M3U playlist

Generated IPTV.M3U channel list currently contains over 18,000 FREE IPTV channels
* Python3 used for aggregating M3U files found elsewhere on the net (see [source code](https://github.com/cdgamlin/cdgamlin.github.io/tree/main/PARS))
* Channel information is parsed from multiple data fields to obtain useful information, such country of origin
* Compilation procedure ensures any URL duplicated between M3U files only occurs once in the final file
* [DOMN:CC] pattern added as suffix to all channel names, which makes it easier to distinguish between similar channels
* "DOMN" are 4 letter codes representing which server group the channel is coming from
* "DOMN" 4 letter codes are generated by the algorithm based on the server name (eg: all https://*.pluto.tv/ are "PLTO")
* "CC" are 2 letter codes representing server country codes (eg: "UK") which can come from server name or group-title info
* "TV" is used as the 2 letter country code if the country is not determinable from the server URL or group-title
* Channels are grouped into category (where possible) or into subcontinent the channel comes from (when category in unobtainable)
* Subcontinents are based more on language groups than geography, to hint what language(s) a channel may be in
* Channels are far from being fully tested, and some links are broken (but there are a lot of excellent channels within this list)
* 10,000 channels come from two BIG M3U playlists
* Other channels come from playlists including: Pluto, Samsung, Plex, Stirr, and country lists from [this site](https://d.tousecurity.com)
* The only countries included from the country list site are: AU, CA, NZ, UK, US
* Unless I get some real demand for it, I will not be adding more countries to the list
* IPTV.m3u generated playlist is at [https://cdgamlin.github.io/IPTV.m3u](https://cdgamlin.github.io/IPTV.m3u)

Email: cdgamlin (ąţ) gmail (ɗδţ) com
