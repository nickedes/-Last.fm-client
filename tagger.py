from mutagen.mp3 import MP3
import os
import sqlite3 as sql
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Last.fm API
my_api_key = "829b12779f358d0af117bef698aaa7e2"

url = "http://ws.audioscrobbler.com/2.0/?"

params = urllib.parse.urlencode(
    {'method': 'user.getFriends', 'user': 'nickedes', 'api_key': my_api_key})

site = urllib.request.urlopen(url + params)

tree = ET.parse(site)
root = tree.getroot()
x = root.find("friends")
users = x.findall("user")


types = []
con = sql.connect('lfm.db')
with con:
    cur = con.cursor()
    for i in users:
        cur.execute("INSERT INTO Users(Name) VALUES(?);", (i.find("name").text,))
    for root, dirs, files in os.walk("/mnt/E4481D43481D1640/Moosik/MAGIC!"):
        for x in files:
            name, _, typ = x.partition('.')
            data = ()
            if typ not in ['jpg', 'png', 'jpeg', 'txt', 'ini', 'db', 'tif']:
                # process file Todo: insert attributes of files in db
                audio = MP3(os.path.join(root, x))
                # data=data+(audio["TIT2"],audio["TPE1"],)
                songtitle = audio["TIT2"].text[0]
                artist = audio["TPE1"].text[0]
                album = audio["TALB"].text[0]
                cur.execute("INSERT INTO Songs(Name,Artist) VALUES(?,?);", (songtitle, artist))
                cur.execute("INSERT INTO Artist(Name) VALUES(?);", (artist,))
                if typ not in types:
                    types.append(typ)
