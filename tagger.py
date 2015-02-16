from mutagen.mp3 import MP3
import os
import sqlite3 as sql
"""
audio = MP3("/mnt/E4481D43481D1640/Moosik/Bollywood/Sham.mp3")
songtitle = audio["TIT2"]
artist = audio["TPE1"]
album = audio["TALB"]
for x in audio:
	print(x,":",audio[x])
"""
ctr=0
types=[]
con = sql.connect('lfm.db')
with con:
	cur = con.cursor()
	for root, dirs, files in os.walk("/mnt/E4481D43481D1640/Moosik/MAGIC!"):
		for x in files:
			name,_,typ=x.partition('.')
			data=()
			if typ not in ['jpg','png','jpeg','txt','ini','db','tif']:
				#process file Todo: insert attributes of files in db
				audio = MP3(os.path.join(root,x))
				#data=data+(audio["TIT2"],audio["TPE1"],)
				songtitle = audio["TIT2"].text[0]
				artist = audio["TPE1"].text[0]
				album = audio["TALB"].text[0]
				cur.execute("INSERT INTO Songs(Name,Artist) VALUES(?,?);",(songtitle,artist))
				cur.execute("INSERT INTO Artist(Name) VALUES(?);",(artist,))
				if typ not in types:
					types.append(typ)
