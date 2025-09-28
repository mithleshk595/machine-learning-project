# import numpy
# speed = [86, 87, 88, 111, 103, 94, 95, 110, 99]
# x = numpy.mean(speed)
# print(x)


# import numpy 
# speed = [90, 99, 98, 100, 101, 89, 97, 78]
# x = numpy.median(speed)
# print(x)


from scipy import stats
speed = [32, 111, 138, 28, 59, 77, 97, 69, 56]
x = stats.mode(speed)
print(x)

