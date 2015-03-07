import urllib2

url = "https://luaforwindows.googlecode.com/files/LuaForWindows_v5.1.4-46.exe"
name = url.split('/')[-1]
f = urllib2.urlopen(url)
with open(('C:\Users\Administrator\Desktop\%s' % name), 'wb') as fid:
    fid.write(f.read())

print "download finished!"
