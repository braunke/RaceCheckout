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
    raceList.append((20, "SoCal", 103.99))
    raceList.append((21, "Palmerton", 123.99))
    raceList.append((22, "Michigan", 104.99))
    raceList.append((23, "Austin", 114.99))
    raceList.append((30, "Breckenridge", 134.99))
    raceList.append((31, "Dallas", 209.99))
    raceList.append((32, "Florida", 123.99))
    raceList.append((33, "Vermont", 144.99))

    for race in raceList:
        createRaces(race)
#createRaceList()
def addRaceToCart(race):
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()

    c.execute('''INSERT INTO Cart
                                 (RACEID)\
                              VALUES(? )''',
              (race,))
    conn.commit()
    conn.close()
#list of races in cart
def cartItems():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACEID from
                              CART''')
    cartRaceID = c.fetchall()
    raceCart = []
    for race in cartRaceID:
        c.execute('''SELECT RACENAME, RACECOST, RACES.RACEID from
                                  RACES
                                  INNER JOIN CART on CART.RACEID = RACES.RACEID WHERE CART.RACEID=?''',(race))
        races = c.fetchall()
        raceCart.append(races)
    return raceCart
#clears cart
def clearCart():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute("DELETE FROM CART")
    conn.commit()
    conn.close()
def cartPriceTotal():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACECOST from RACES
              INNER JOIN CART on CART.RACEID = RACES.RACEID ''')
    costs = c.fetchall()
    totalCost = 0
    for race in costs:
        cost = (race[0])
        totalCost += cost
    displayCost =(round(totalCost, 2))
    return displayCost
def removeCartItem(race):
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute("DELETE FROM CART WHERE RACEID =?",(race,))
    conn.commit()
    conn.close()
