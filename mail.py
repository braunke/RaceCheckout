from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import os
import dbFunctions
from flask import Flask, render_template
#help with mail stuff, plus from group work
#https://stackoverflow.com/questions/42136418/send-html-email-using-flask-in-python


def sendRaceEmail(receiver):
    sender = "pythoncapstoneracing@gmail.com"
    sender_password = 'dbkokomo27'#os.environ.get('EMAIL_PASSWORD')

    total, discount = dbFunctions.cartPriceTotal()
    cartItems = dbFunctions.cartItems()
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Spartan Race Sign Up"
    msg['From'] = sender
    msg['To'] = receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = render_template('emailForm.txt', total = total, cartItems= cartItems)
    html = render_template('emailForm.html', total = total, cartItems= cartItems)

    plain_text_message = MIMEText(text, 'plain')
    html_message = MIMEText(html, 'html')

    msg.attach(plain_text_message)
    msg.attach(html_message)

    # Send the message via the gmail server. Update as needed
    s = SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(sender, sender_password)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()
