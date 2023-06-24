# [cdgamlin.github.io](https://cdgamlin.github.io)

# PARS: *Playlist Aggregator Refiner Scheme*

Parses multiple FREE online M3U playlists to generate a custom IPTV.M3U playlist

Generated IPTV.M3U channel list currently contains over 18,000 FREE IPTV channels
* Python3 used for compiling M3U files found elsewhere on the net (see source code)
* Compilation procedure ensures that any URL duplicated between M3U files only occurs once in the final file
* [DOMN:CC] added as suffix to all channel names (to make it easy to determine between similar channels)
* "DOMN" are 4 letter codes representing which server group the channel is coming from (eg: "PLTO")
* "ZYZX" is used as the 4 letter code for all server groups that have few (currently <10) channels
* "CC" are 2 letter codes representing server country codes (eg: "UK")
* "TV" is used as the 2 letter country code if the country is not determinable from the server URL
* Channels are far from being fully tested - but there are a lot of excellent channels within this list
* 10,000 channels come from two BIG M3U playlists
* Other playlists include: Pluto, Samsung, Plex, Stirr, and country lists from [this site](https://d.tousecurity.com)
* From the county lists, I have only included AU, CA, NZ, UK, US
* I'll leave it to others to add more countries to the [source.txt](https://github.com/cdgamlin/cdgamlin.github.io/tree/main/PARS) list (if they wish)
* List accessible via [https://cdgamlin.github.io/IPTV.m3u](https://cdgamlin.github.io/IPTV.m3u)
* Source code accessible [here](https://github.com/cdgamlin/cdgamlin.github.io/tree/main/PARS)

Email: cdgamlin (ąţ) gmail (ɗδţ) com
