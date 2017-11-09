import urllib2

url = "https://api.nasa.gov/planetary/apod?api_key=2GTxH8djyXY3fq4DXGy5nY7o6OPAZq3oAhq53opG"
site = urllib2.urlopen(url)
s = site.read()
s_split = s.split('\n')
s_dict = []
for i in s_split:
    s_dict.append(i.split(':',1))
d = {}
for i in s_dict:
    if len(i) >= 2:
        d[i[0]] = i[1]


