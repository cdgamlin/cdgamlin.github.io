# [cdgamlin.github.io](https://cdgamlin.github.io)

# PARS: *Playlist Aggregator Refiner Scheme*

Parses multiple FREE online M3U playlists to generate a custom IPTV.M3U playlist

Generated IPTV.M3U channel list currently contains over 18,000 FREE IPTV channels
* Python3 used for compiling M3U files found elsewhere on the net (see [source code](https://github.com/cdgamlin/cdgamlin.github.io/tree/main/PARS))
* Compilation procedure ensures that any URL duplicated between M3U files only occurs once in the final file
* [DOMN:CC] pattern added as suffix to all channel names (makes it easy to distinguish between similar channels)
* "DOMN" are 4 letter codes representing which server group the channel is coming from (eg: "PLTO")
* "ZYZX" is used as the 4 letter code for all server groups that have few (currently <10) channels
* "CC" are 2 letter codes representing server country codes (eg: "UK")
* "TV" is used as the 2 letter country code if the country is not determinable from the server URL
* Channels are far from being fully tested - but there are a lot of excellent channels within this list
* 10,000 channels come from two BIG M3U playlists
* Other channels come from playlists including: Pluto, Samsung, Plex, Stirr, and country lists from [this site](https://d.tousecurity.com)
* The only countries included from the country list are: AU, CA, NZ, UK, US
* If anyone wants to add more countries to [source.txt](https://github.com/cdgamlin/cdgamlin.github.io/tree/main/PARS) then I am happy for them to do so
* IPTV.m3u generated playlist is at [https://cdgamlin.github.io/IPTV.m3u](https://cdgamlin.github.io/IPTV.m3u)

Email: cdgamlin (ąţ) gmail (ɗδţ) com
