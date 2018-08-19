import time
import sqlite3
from sense_hat import SenseHat
dbname='logger.db'
sampleFreq = 1

def getSenseHatData():
    sense = SenseHat()
    temp = sense.get_temperature()
    humid = sense.get_humidity()
    if temp is not None:
        temp = round(temp, 1)
        logData (temp,humid)

def logData (temp,humid):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO LOGGER_data values(datetime('now'), (?), (?))",(temp,humid))
    conn.commit()
    conn.close()

# display database data
def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM LOGGER_data"):
        print (row)
    conn.close()

def main():
    for i in range (0,5):
        getSenseHatData()
        time.sleep(sampleFreq)
    displayData()

# Execute program
main()
