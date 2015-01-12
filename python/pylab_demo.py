from pylab import *
from numpy.random import *

figure(1)
x = arange(0.0, pi * 2, 0.01)
y1, y2 = sin(x), cos(x)
subplot(121)
plot(x, y1)
subplot(122)
plot(x, y2)

figure(2)
x = arange(0.0, pi * 2, 0.01)
y1, y2 = sin(x), cos(x)
subplot(121)
plot(x, y1, 'r-')
subplot(122)
plot(x, y2, 'r-')

show() #very important, or the plot result will not show
