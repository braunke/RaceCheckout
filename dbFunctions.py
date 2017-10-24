import sqlite3
import math

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
#deletes one race cart item
def removeCartItem(race):
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute("DELETE FROM CART WHERE RACEID =?",(race,))
    conn.commit()
    conn.close()
#just gets list of race ids from cart
def cartList():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACEID from
                                  CART''')
    cartRaceID = c.fetchall()
    cartList = []
    for races in cartRaceID:
        cartList.append(races[0])
    return cartList
#checks if the user gets a discount
def discountOnRaces(cartList):
    newCartList = []
    for race in cartList:
        #only wanted the fist number since that id's what kind of race it is
        id = race / 10
        id = math.floor(id)
        newCartList.append(id)
    discount = 1
    if 1 in newCartList:
        if 2 in newCartList:
            if 3 in newCartList:
                discount = .75
    return (discount)
#calculates cart cost
def cartPriceTotal():
    conn = sqlite3.connect('raceInfo.db')
    c = conn.cursor()
    c.execute('''SELECT RACECOST from RACES
              INNER JOIN CART on CART.RACEID = RACES.RACEID ''')
    costs = c.fetchall()
    cartIds = cartList()
    discount = discountOnRaces(cartIds)
    totalCost = 0
    for race in costs:
        cost = (race[0])
        totalCost += cost
    amountOff = totalCost * discount
    displayCost =(round(amountOff, 2))
    return displayCost ,discount
