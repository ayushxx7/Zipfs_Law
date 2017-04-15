#modify paths and names according to your file paths and names.

import fileinput

def Rep(name):
    try:
        with fileinput.FileInput(name+'.txt', inplace=True, backup='.bak') as file:
            for line in file:
                #print(line)
                print(line.replace('[br]', ' '), end='')
                #print(line)
               # print(line.replace('...', ' '), end='')
               ## print(line.replace('..', ' '), end='')
                #print(line.replace('.', ' '), end='')
                #print(line.replace('[', ' '), end='')
               # print(line.replace(']', ' '), end='')


    except FileNotFoundError as e:
        print("ERROR: " + str(e))
        pass
