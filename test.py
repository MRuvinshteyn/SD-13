import urllib2,json

query = raw_input("Input query here: ")
site = urllib2.urlopen('http://apilayer.net/api/detect?access_key=e75477049e4a7f0e06d4a416a1924b84&query=' + query)
s = site.read()
json = json.loads(s)

if json['success']:
    for item in json['results']:
        print item['language_code']
        print item['language_name']