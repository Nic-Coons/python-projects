import sqlite3
import time
import datetime


conn = sqlite3.connect('tutorial2.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE practice1(ID INTEGER PRIMARY KEY, unix REAL, datestamp TEXT, keyword TEXT) ")

keyword = 'File Mover'

def dataEntry():
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO practice1 (unix, datestamp, keyword) VALUES (?, ?, ?)",(time.time(), date, keyword))
    conn.commit()

sql = "SELECT * FROM practice1 WHERE keyword =?"

wordUsed = 'File Mover'

def readData():
    for row in c.execute(sql, [(wordUsed)]):
        print (row)
