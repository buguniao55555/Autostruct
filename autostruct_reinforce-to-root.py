import time
import random
print("Author:Buguniao55555\nGithub link: https://github.com/buguniao55555/Autostruct\n")
time.sleep(1)
filename = str(input('\nplease write your file name(without the .craft name)\nexample: test1\n'))
f = open(filename+'.craft', "r", encoding='UTF-8')
data = f.readlines()
print('loading')
def writeD(current,new):
    cid = 0
    string = ''
    rf = open(filename+'.craft', "r+", encoding='UTF-8')
    for orig in rf.readlines():
        if orig == current:
            string += new
        else:
            string += orig
        cid+=1
    rf.close()
    wf=open(filename+'.craft','w+', encoding='UTF-8')
    wf.write(string)
    wf.close()
b = int(input("what type of reinforcement do you want?\n1.None\n2.Root\n3.Motherpart\n4.Heaviest\nPlease input your number of choice\n"))
if b == 1:
    writeD('\tautostrutMode = Off\n','\tautostrutMode = Off\n')
    writeD('\tautostrutMode = Root\n','\tautostrutMode = Off\n')
    writeD('\tautostrutMode = Grandparent\n','\tautostrutMode = Off\n')
    writeD('\tautostrutMode = Heaviest\n','\tautostrutMode = Off\n')
    writeD('\trigidAttachment = False\n','\trigidAttachment = True\n')
elif b == 2:
    writeD('\tautostrutMode = Off\n','\tautostrutMode = Root\n')
    writeD('\tautostrutMode = Root\n','\tautostrutMode = Root\n')
    writeD('\tautostrutMode = Grandparent\n','\tautostrutMode = Root\n')
    writeD('\tautostrutMode = Heaviest\n','\tautostrutMode = Root\n')
    writeD('\trigidAttachment = False\n','\trigidAttachment = True\n')
elif b == 3:
    writeD('\tautostrutMode = Off\n','\tautostrutMode = Grandparent\n')
    writeD('\tautostrutMode = Root\n','\tautostrutMode = Grandparent\n')
    writeD('\tautostrutMode = Grandparent\n','\tautostrutMode = Grandparent\n')
    writeD('\tautostrutMode = Heaviest\n','\tautostrutMode = Grandparent\n')
    writeD('\trigidAttachment = False\n','\trigidAttachment = True\n')
elif b == 4:
    writeD('\tautostrutMode = Off\n','\tautostrutMode = Heaviest\n')
    writeD('\tautostrutMode = Root\n','\tautostrutMode = Heaviest\n')
    writeD('\tautostrutMode = Grandparent\n','\tautostrutMode = Heaviest\n')
    writeD('\tautostrutMode = Heaviest\n','\tautostrutMode = Heaviest\n')
    writeD('\trigidAttachment = False\n','\trigidAttachment = True\n')
print('done\nexit in five seconds')
time.sleep(5)

