#disclaimer: File paths are system dependent, change code according to your location and name for subs.
#run this file and then run Plotter.py

import os
import fileinput
from collections import Counter

from Replacer import Rep
from Counter import Count

punc = list("{()}\\<—-—...,>-./;?&-..!0123456789:%\"")
cnt = 1

#path where subs are stored
path = 'C:\South\S'  
N = path+'onetoEighteenModified'   #replace this for every test, will modify this part later on so that if file name exists it automatically changes to a different name by appending a digit at the end.
while cnt != 19:

    #N = input('Name of Processing Text File? ')
    #N = path+str(cnt)
    #print(N)
    for file in os.listdir(path+str(cnt)):
        #print(file)
        str_link = open(path+str(cnt)+'\\'+file,'r').read()
        #print(str_link)
        f2 = open(N+'.txt','a')
        #f2 is final file with all processed data
       # print('opened')
#str_link = "ffff, hhhh, & tommorow home, Have you from gone?"
        for line in str_link:
            if line in punc:
                str_link = str_link.replace(line," ")
        str_link = str_link.lower()
        f2.write(str_link)
       # print('written')
        f2.close()

    # Rep(N)
    # # #print('called Replacer')
    # Count(N)
    # # #print('called Counter')
    cnt += 1


#may not be required for your subs

Rep(N) #to replace [br] with spaces

#may not be required for your subs

#
# # print('called Replacer')


Count(N) #for frequency mapping in descending order and putting data in a csv file.



'''

for i in str_link.split(' '):
    if '[br]' in i:
        #print(i)
        print(i.index('['))
        x = i.index('[')
        i = i[:x] + ' ' + i[x + 4:]
        print(i)
'''


       # print(i)
# f2.write(str_link)
# f2.close()
#
# print(str_link)
# for i in str_link.split(' '):
#     l.append(i)
#
# print(l)