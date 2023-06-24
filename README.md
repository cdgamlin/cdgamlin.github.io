# cdgamlin.github.io

# PARS: *Playlist Aggregator Refiner Scheme*

Parses FREE online M3U playlists and generates a custom IPTV.M3U playlist

Generated IPTV.M3U channel list currently contains over 18,000 Free IPTV channels
* Scraped and compiled with Python3 from some large M3U files found elsewhere on the net (see source code)
* Compilation ensures that any URL duplicated across M3U files is occurs only once in the final M3U
* [DOMN:CC] added as suffix to all channel names
* "DOMN" are 4 letter codes representing which server group the channel is coming from (eg: "PLTO")
* "ZYZX" is used as the 4 letter code for all server groups that have few (currently <10) channels
* "CC" are 2 letter codes representing server country codes (eg: "UK")
* "TV" is used as the 2 letter country code if the country is not determinable from the server URL
* Channels are far from being fully tested - but there are a lot of excellent channels within this list
* List accessible via [https://cdgamlin.github.io/IPTV.m3u](https://cdgamlin.github.io/IPTV.m3u)
* Source code accessible via [My Google Drive](https://colab.research.google.com/drive/1tVaR-fExszrBF_4SSelNrl8lQr-R8rwd#scrollTo=qtIIhjyKU3-k)
* Currently includes channels scraped from: Pluto, Samsung, Plex, Stirr, AU, CA, NZ, UK, US, and "the two BIG lists"

Email: cdgamlin (ąţ) gmail (ɗδţ) com
