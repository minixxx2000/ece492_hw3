from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = sin(2*pi*t)

figure(1)
clf()
plot(t,y)

xlabel('Time (s)')
ylabel('$y(t)$')

savefig('myfig.png',dpi = 300)

show()

#input("Press Return")  #run in the Windows

