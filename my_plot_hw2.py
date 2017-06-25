from matplotlib.pyplot import *
from numpy import *

t = arange(1,3,0.02)
T = 6*log(t)-(7*e**(0.2*t))

figure(1)
clf()
plot(t,T)

xlabel('Time(min)')
ylabel('Temperature(Celsius)')
title('Chia-Han, Chen Plot')
savefig('myfig_hw2.png',dpi = 300)

show()
