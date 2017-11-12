#Michael Ruvinshteyn
#SoftDev1 pd7
#HW14 -- Getting More REST
#2017 - 11 - 12

from flask import Flask, render_template, request
import urllib2,json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("lang_det_query.html")

@app.route('/det', methods=['GET','POST'])
def lang():
    query = request.form['query']
    url = "http://apilayer.net/api/detect?access_key=e75477049e4a7f0e06d4a416a1924b84&query=" + query
    site = urllib2.urlopen(url)
    s = site.read()
    stuff = json.loads(s)
    if (stuff['success']):
        return render_template('lang_det_display_success.html', QUERY = query, langs = stuff['results'])
    else:
        return render_template('lang_det_display_failure.html', ERROR = "invalid input")
    
if __name__ == "__main__":
    app.debug = True
    app.run()
