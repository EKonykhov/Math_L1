import numpy
import matplotlib.pyplot as p

x = numpy.arange(-10, 10, 0.1)

k1 = 1
k2 = 2

p.plot(x, numpy.cos(k1*x))
p.plot(x, numpy.cos(k2*x))

p.title(f'две кривые y(k,x)=cos(k∙x), где k1 = {k1}, k2 = {k2}')
p.grid(True)

p.show()

