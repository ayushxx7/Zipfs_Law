#modify paths and names according to your file paths and names.


from collections import Counter

def Count(Name):
    test = open(Name+'.txt','r').read()
    x = Counter(test.split())
#print(x)

# f = open('s1FreqTest.txt','w')
# f.close()
# with open("s1FreqTest.txt") as f:
#     for k,v in  x.most_common():
#         f.write( "{} {}\n".format(k,v) )
# f = open('abc','w').close()
# with open("abc") as f:
# for k,v in  x.most_common():
#     print( "{} {}\n".format(k,v) )


#print(x['i\'ll'])

    #z = input('Name of csv file? ')
    z = Name
    i = 1
    with open(z+'.csv','w') as ts:
        for k, v in x.most_common():
            ts.write("{0},{1},{2}\n".format(k, v, i))
            i += 1