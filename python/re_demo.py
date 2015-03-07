#encoding:utf-8
import re

m = re.search('\d', '1a2b3c4d')
#print m.group()

p = re.compile('\d')
alls = p.finditer('1a2b3c4d')
#all.next() except StopIteration:
alls.next().group()
for i in alls:
    print i.group()
    print i.start()

print re.findall('\d', '1a2b3c4d')
