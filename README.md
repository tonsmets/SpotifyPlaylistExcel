SpotifyPlaylistExcel
===============
Convert Spotify song URLs to a Excel spreadsheet

# Overview
I wrote this script because I needed a way to share a playlist with non-Spotify users.

# Usage
In Spotify: select the playlist, then select all songs. Now simply press (CMD or CTRL) + C, then use Notepad or whatever and paste the "songs" here (CMD or CTRL) + V. Now save this file as **input.txt**!

```
https://open.spotify.com/track/7o2CTH4ctstm8TNelqjb51
https://open.spotify.com/track/3YBZIN3rekqsKxbJc9FZko
https://open.spotify.com/track/0bVtevEgtDIeRjCJbK3Lmv
https://open.spotify.com/track/53968oKecrFxkErocab2Al
https://open.spotify.com/track/0ZEhlT9v8CdOKu55zhYGv9
```

To run the script simply type: `python3 scrapeSpotify.py`

# Dependencies
To run the script install the following dependencies: beautifulsoup4, requests, json, xlwt

# Disclaimer
At the time I wrote this I simply made the functionality that I need. I am in no way responsible for malfunctioning of this piece of code