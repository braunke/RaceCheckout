import sqlite3
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
def showRaces():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACEID, RACENAME, RACECOST from
                          RACES''')
    raceList=list(c.fetchall())
    print(raceList)
    return raceList
#showRaces()
def deleteRows():

        conn = sqlite3.connect('raceInfo.db')
        cursor = conn.execute('DELETE FROM RACES WHERE RACENAME= ?',("Minnesota",))
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
    raceList.append((11, "Chicago", 99.99))
    raceList.append((12, "San Jose", 99.99))
    raceList.append((13,"Ashville", 103.99))
    raceList.append((10, "Minnesota", 89.99))
    print(raceList)
    for race in raceList:
        createRaces(race)
#createRaceList()
def addRaceToCart(race):
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    print(race)
    c.execute('''INSERT INTO Cart
                                 (RACEID)\
                              VALUES(? )''',
              (race,))
    conn.commit()
    conn.close()
def cartItems():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACEID from
                              CART''')
    cartRaces = c.fetchall()
    raceCart = []
    for race in cartRaces:
        c.execute('''SELECT RACENAME, RACECOST from
                                  RACES
                                  INNER JOIN CART on CART.RACEID = RACES.RACEID WHERE CART.RACEID=?''',(race))
        races = c.fetchall()
        raceCart.append(races)
    print(raceCart)
    return raceCart
cartItems()
