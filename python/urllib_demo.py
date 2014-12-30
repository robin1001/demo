import urllib

params = urllib.urlencode({'q': keyword})
data = urllib.urlopen("http://www.zdic.net/sousuo/", params).read().decode('gbk') #encoding optional

