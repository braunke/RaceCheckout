from flask import Flask, render_template, flash, session, redirect, request, url_for
app = Flask(__name__)
import database


@app.route('/')
def hello_world():
    raceList = database.showRaces()
    cartItems = database.cartItems()
    return render_template('homePage.html', raceList=raceList, cartItems=cartItems)
@app.route('/save', methods=['POST'])
def saveSearch():
    raceName = request.form['raceName']
    database.addRaceToCart(raceName)
    print(raceName)
    return redirect('/')
@app.route('/update', methods=['POST'])
def updateCart():
    return redirect('/')
if __name__ == '__main__':
    app.run()
