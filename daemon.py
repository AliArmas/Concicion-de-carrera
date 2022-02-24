#Librerias
from threading import *
import threading
import time 



def hilo_1():
    for x in range(5) :
        print('sin')
        time.sleep(2.0)

t1 = Thread(target=hilo_1)
t1.setDaemon(True)
t1.start()

time.sleep(10)
print("Hilo principal")