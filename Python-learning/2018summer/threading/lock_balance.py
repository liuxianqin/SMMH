#coding=utf-8
import time,threading

balance=100
lock=threading.Lock()

def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join() #如果thread是某个子线程，则调用thread.join()的作用是确保thread子线程执行完毕后才能执行下一个线程。
t2.join()
print(balance)
