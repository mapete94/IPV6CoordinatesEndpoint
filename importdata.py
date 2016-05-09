import sqlite3
import csv
i=1;
conn = sqlite3.connect("db.sqlite3")

c = conn.cursor()

reader = csv.reader(open('GeoLiteCityv6.csv', 'r'), delimiter = ',')
for row in reader:
    to_db = [i, unicode(row[7], "utf8"), unicode(row[8], "utf8"), unicode(row[0], "utf8"), unicode(row[1], "utf8")]
    c.execute("INSERT INTO endpoint_coordinates VALUES (?, ?, ?, ?, ?);", to_db)
    i+=1
print to_db
# c.execute("INSERT INTO endpoint_coordinates VALUES (3, 0.0, 1.2, '1', '2')")

conn.commit()

conn.close()