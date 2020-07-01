import random
import time

ACCELEROMETER_FILE = '/sensors/accelerometer/data'


f=open (ACCELEROMETER_FILE)
a=f.readline()
lista=a.split(",")

z = int(lista[2])

if z > 0: 
    print('orizzontale')
else: 
    print ('verticale')
