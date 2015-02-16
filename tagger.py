from mutagen.mp3 import MP3
import os
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
for root, dirs, files in os.walk("/mnt/E4481D43481D1640/Moosik"):
	for x in files:
		name,_,typ=x.partition('.')
		if typ not in ['jpg','png','jpeg','txt','ini','db','tif']:
			#process file Todo: insert attributes of files in db
			print(x)
			if typ not in types:
				types.append(typ)
			ctr=ctr+1
print(ctr)
print(types)