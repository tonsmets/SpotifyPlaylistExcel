import bs4
import requests
import json
import sys
import xlwt
import datetime
import time

with open('input.txt') as f:
	lines = [line.rstrip('\n') for line in open('input.txt')]

songCount = len(lines)

wb = xlwt.Workbook()
ws = wb.add_sheet('Spotify Playlist')

head_style = xlwt.easyxf('font: bold on');

ws.write(0, 0, "Song", head_style)
ws.write(0, 1, "Artist", head_style)

maxTitleLength = 0
maxArtistLength = 0

startTime = datetime.datetime.now()

for x in range(0, songCount):
	title = ""
	artist = ""
	try:
		response = requests.get(lines[x])
	except requests.exceptions.ConnectionError as ce:
		print("Failed to connect to '{0}'".format(lines[x]),"{0}".format(ce))

	try:
		soup = bs4.BeautifulSoup(response.text)
		soup.encode('utf-8')
	except:
		print("Unable to parse HTML","{0}".format(sys.exc_info()[0]))

	try:
		fullText = soup.title.get_text().replace(", a song by ", "#####").replace(" on Spotify", "")
		title = fullText.split("#####")[0]
		artist = fullText.split("#####")[-1]
		if(len(title) > maxTitleLength):
			maxTitleLength = len(title)
		
		if(len(artist) > maxArtistLength):
			maxArtistLength = len(artist)
		
		ws.write(x+1, 0, title)
		ws.write(x+1, 1, artist)
	except:
		print("[IGNORING] Title not found","{0}".format(sys.exc_info()[0]))
		pass

	print("[SCRAPED] {0} by {1}".format(title, artist))

# Set the column width to roughly the right size
ws.col(0).width = 256 * maxTitleLength
ws.col(1).width = 256 * maxArtistLength

endTime = datetime.datetime.now()
deltaTime = endTime - startTime
deltaTime = int(deltaTime.total_seconds() * 1000)

print("Scraped {0} songs in {1}ms".format(songCount, deltaTime))

ws.write(songCount+2, 0, "Generated in " + str(deltaTime) + "ms at " + time.strftime("%d/%m/%Y %H:%M:%S"))
ws.write(songCount+3, 0, "https://github.com/tonsmets/SpotifyPlaylistExcel")

wb.save("playlist.xls")