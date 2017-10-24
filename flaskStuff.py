from flask import Flask, render_template, flash, session, redirect, request, url_for
app = Flask(__name__)
import database


@app.route('/')
def hello_world():
    sprintRaceList = database.showRaces('1%')
    superRaceList = database.showRaces('2%')
    beastRaceList = database.showRaces('3%')
    total = database.cartPriceTotal()
    cartItems = database.cartItems()
    Message = None
    discount = database.discountOnRaces
    if discount != 1:
        Message = "25% discount for signing up for a Trifecta!"
    return render_template('homePage.html', Message = Message, sprintRaceList=sprintRaceList, superRaceList=superRaceList, beastRaceList=beastRaceList, cartItems=cartItems, total = total)
@app.route('/save', methods=['POST'])
def saveSearch():
    raceName = request.form['raceName']
    database.addRaceToCart(raceName)

    return redirect('/')

@app.route('/delete', methods=['POST'])
def clearCart():
    database.clearCart()
    return redirect('/')
@app.route('/remove', methods=['POST'])
def removeCartItem():
    race = request.form['removeRaceItem']
    database.removeCartItem(race)
    return redirect('/')
if __name__ == '__main__':
    app.run()
