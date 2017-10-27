import sqlite3
import math
#database to store race info and result info
def createDatabase():
    try:
        conn = sqlite3.connect('raceInfo.db')



        conn.execute('''CREATE TABLE RACES
                                         (
                                         RACEID INT PRIMARY KEY ,
                                         RACENAME TEXT,
                                         RACECOST FLOAT    
                                         );''')
        conn.execute('''CREATE TABLE RACETypes
                                                 (
                                                 RACEID INT,
                                                 RACENAME TEXT,
                                                 FOREIGN KEY(RACEID)REFERENCES RACES(RACEID)
                                                 
                                                 );''')
        conn.execute('''CREATE TABLE CART
                                            ( 
                                            RACEID INT, 
                                            FOREIGN KEY(RACEID)REFERENCES RACES(RACEID)
                                            )''')
        conn.close()
    except sqlite3.OperationalError as err:
        print(err)
        print("The database already exists")
#createDatabase()
def showRaces(type):
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACEID, RACENAME, RACECOST from
                          RACES WHERE RACEID LIKE ? ''', (type,))
    raceList=list(c.fetchall())
    return raceList
#showRaces()
def deleteRows():

        conn = sqlite3.connect('raceInfo.db')
        cursor = conn.execute('DELETE FROM RACES ')
        # uses rowcount to see if a row was affected
        deleteStatus = (cursor.rowcount)
        # depending on if rows were affected or not a message will print
        if deleteStatus == 0:
            print("This product is not in the database")
        elif deleteStatus == 1:
            print("Row was deleted")
        conn.commit()
        conn.close()
#deleteRows()
def createRaces(race):
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''INSERT INTO RACES
                             (RACEID, RACENAME, RACECOST)\
                          VALUES(?,?, ? )''',
              (race))
    conn.commit()
    conn.close()
#createRaces()
def createRaceList():
    raceList = []
    raceList.append((11, "Chicago Sprint", 99.99))
    raceList.append((12, "San Jose Sprint", 99.99))
    raceList.append((13,"Ashville Sprint", 103.99))
    raceList.append((10, "Minnesota Sprint", 89.99))
    raceList.append((20, "SoCal Super", 103.99))
    raceList.append((21, "Palmerton Super", 123.99))
    raceList.append((22, "Michigan Super", 104.99))
    raceList.append((23, "Austin Super", 114.99))
    raceList.append((30, "Breckenridge Beast", 134.99))
    raceList.append((31, "Dallas Beast", 209.99))
    raceList.append((32, "Florida Beast", 123.99))
    raceList.append((33, "Vermont Beast", 144.99))

    for race in raceList:
        createRaces(race)
#createRaceList()


