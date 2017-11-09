#Michael Ruvinshteyn
#SoftDev1 pd7
#HW13 -- A RESTful Journey Skyward
#2017 - 11 - 09

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

url = "https://api.nasa.gov/planetary/apod?api_key=2GTxH8djyXY3fq4DXGy5nY7o6OPAZq3oAhq53opG" #URL for the API key
site = urllib2.urlopen(url) #opens API key and obtains all of its contents
s = site.read() #creates a string of all of the key's contents
d = json.loads(s) #creates a dictionary with all of the values obtained from the key

#OBTAIN ALL VALUES TO BE DISPLAYED IN THE TEMPLATE#
name = d['copyright']
img = d['url']
desc = d['explanation']
date = d['date']
title = d['title']

@app.route('/')
def home():
    return render_template("api.html", NAME = name, IMG = img, EXP = desc, DATE = date, TITLE = title)

if __name__ == "__main__":
    app.debug = True
    app.run()
