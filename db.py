import sqlite3 as sql
con = sql.connect('lfm.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Songs(Name TEXT ,Artist TEXT )")
    cur.execute("CREATE TABLE Artist(Name TEXT )")
    cur.execute("CREATE TABLE Users(Name TEXT PRIMARY KEY)")
