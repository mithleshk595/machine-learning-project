# import numpy
# speed = [86, 87, 88, 111, 103, 94, 95, 110, 99]
# x = numpy.std(speed)
# print(x)

# import numpy
# speed = [32,111,138,28,59,77,97]
# x = numpy.std(speed)
# print(x)


# import numpy
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# x = numpy.percentile(ages, 75)
# print(x)

import numpy 
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)
