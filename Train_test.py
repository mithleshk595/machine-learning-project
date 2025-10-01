import numpy
import matplotlib.pylab as plt
numpy.random.seed(0)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)

plt.scatter(x,y)
plt.show()
