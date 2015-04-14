

from ConfigParser import *



config = ConfigParser()
config.read('config.conf')


name = config.get('userinfo', 'name')
pwd = config.get('userinfo', 'pwd')

print name, pwd


