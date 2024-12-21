import time, random as r
import threading

def task(lb,ub,refreshTime,displayLocation):
    while True:
        num=r.randint(lb,ub)
        display(num,displayLocation)
        time.sleep(refreshTime)
    return

t1=threading.Thread(target=task, args=(10,20,10,D1,))
t2=threading.Thread(target=task, args=(10,20,10,D1,))
t3=threading.Thread(target=task, args=(10,20,10,D1,))
t4=threading.Thread(target=task, args=(10,20,10,D1,))
t5=threading.Thread(target=task, args=(10,20,10,D1,))
t6=threading.Thread(target=task, args=(10,20,10,D1,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
