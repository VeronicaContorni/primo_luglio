import random
import time

f=open ('pluto.data','w')
for i in range (10):
    print("Ciao sono Pluto")
    a=(random.random()*2)
    time.sleep(a)
    f.write(str(a)+' ')
f.close()
