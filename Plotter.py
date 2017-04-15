#____________________________________________
#                                           #
#       Ziph's law has been verified        #
#                                           #
#___________________________________________#

#modify paths and names according to your file paths and names.

from csv import reader
from matplotlib import pyplot

path = 'C:\South\S'
N = path+'onetoEighteenModified.csv'

with open(N, 'r') as f:
    data = list(reader(f))

x = 1
temp = [24843/int(i[2]) for i in data]

for i in data:
    print(i[2])

# x = 1
# for i in data:
#     i2 = int(i[1])/x
#     temp2 = i2
#     x += 1
#print(temp)

#change range according to your will :)

pyplot.plot(range(len(temp[0:20])), temp[0:20])
pyplot.show()
# import time
# time.sleep(5)
pyplot.yscale('log')
pyplot.xscale('log')
pyplot.plot(range(len(temp[0:24000])), temp[0:24000])
#pyplot.plot(range(len(temp2[0:15000])), temp2[0:15000])
pyplot.show()


