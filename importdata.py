import sqlite3
import csv
"""
one time use script to read csv and put into db
reads csv and identifies unique lat lng pairs counts instances
of pairs and then stores lat lng pairs and their counts in db
only works on empty db
"""
conn = sqlite3.connect("db.sqlite3")
dictlatng={}
c = conn.cursor()

reader = csv.reader(open('GeoLiteCityv6.csv', 'r'), delimiter=',')
for row in reader:
    latlng = (unicode(row[7], "utf8"), unicode(row[8], "utf8"))
    if dictlatng.has_key(latlng):
        dictlatng[latlng] += 1
    else:
        dictlatng[latlng] = 1

i = 1
for key in dictlatng.keys():
    to_db = [i, key[0], key[1], dictlatng[key]]
    c.execute("INSERT INTO endpoint_coordinates VALUES (?, ?, ?, ?);", to_db)
    i += 1

conn.commit()

conn.close()