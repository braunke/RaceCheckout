from flask import Flask, render_template, flash, session, redirect, request, url_for
app = Flask(__name__)
import database
import dbFunctions
import mail

@app.route('/')
def homePage():
    sprintRaceList = database.showRaces('1%')
    superRaceList = database.showRaces('2%')
    beastRaceList = database.showRaces('3%')
    total, discount = dbFunctions.cartPriceTotal()
    cartItems = dbFunctions.cartItems()
    Message = ''
    if discount != 1:
        Message = "25% discount for signing up for a Trifecta!"
    return render_template('homePage.html', Message = Message, sprintRaceList=sprintRaceList, superRaceList=superRaceList, beastRaceList=beastRaceList, cartItems=cartItems, total = total)
@app.route('/save', methods=['POST'])
def saveSearch():
    raceName = request.form['raceName']
    dbFunctions.addRaceToCart(raceName)
    return redirect('/')
@app.route('/delete', methods=['POST'])
def clearCart():
    dbFunctions.clearCart()
    return redirect('/')
@app.route('/remove', methods=['POST'])
def removeCartItem():
    race = request.form['removeRaceItem']
    dbFunctions.removeCartItem(race)
    return redirect('/')
@app.route('/confirm', methods=['POST'])
def confirmationPage():
    total, discout = dbFunctions.cartPriceTotal()
    cartItems = dbFunctions .cartItems()
    if total > 0:
        return render_template('confirmation.html', total = total, cartItems=cartItems)
    else:
        return redirect('/')

@app.route('/email', methods=['GET', 'POST'])
def sendEmail():
    if request.method == 'POST':
        receiver = request.form['email']
        mail.sendRaceEmail(receiver)
        dbFunctions.clearCart()
    return render_template("emailPage.html")

if __name__ == '__main__':
    app.run()
