import numpy
import matplotlib.pylab as plt
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 50)
plt.show()

