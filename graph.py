import numpy
import matplotlib.pylab as plt
x = numpy.random.normal(5.5, 5.0, 100000)
plt.hist(x,5)
plt.show()