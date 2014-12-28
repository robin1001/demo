from pylab import *

x = arange(0.0, math.pi * 2, 0.01)
y = sin(x)
plot(x, y)
show() #very important, or the plot result will not show
