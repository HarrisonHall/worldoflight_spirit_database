# search.py
# TODO

import sys, csv

try:
    import sqlite3
    #conn = sqlite3.connect("spirits.csv")
    print("Opened Database")
except:
    print("Unsuccessful")
    sys.exit(0)

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (Spirit, Artwork Origin);") # use your column names here

with open('spirits.csv','r') as fin: 
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Spirit']) for i in dr]

cur.executemany("INSERT INTO t (Spirit) VALUES (?);", to_db)
con.commit()
cursor = con.execute("SELECT Spirit from t")
for row in cursor:
   print("name =", row[0])


con.close()
