import sqlite3 as lite
import sys
con = lite.connect('logger.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS LOGGER_data")
    cur.execute("CREATE TABLE LOGGER_data(timestamp DATETIME, temperature NUMERIC, humidity NUMERIC)")