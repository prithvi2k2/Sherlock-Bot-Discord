'''
Efforts to keep the bot alive 24/7 with zero cost!!
We can speed up the bot, and guarantee 24/7 if we had funds(we don't have!)
'''
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I don't know how you landed here, Donations are massively appreciated.\nDonations do speed me up!!"

def run():
  app.run(host='0.0.0.0',port=8080)

def dont_die():
    t = Thread(target=run)
    t.start()