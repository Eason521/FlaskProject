
# 多进程
# import gevent
# def fun1():
#     for i in range(5):
#         print("fun 1 this is %s"%i)
#         gevent.sleep(5)
#
# def fun2():
#     for i in range(5):
#         print("fun 2 this is %s"%i)
#         gevent.sleep(10)
#
# t1 = gevent.spawn(fun1)
# t2 = gevent.spawn(fun2)
#
# gevent.joinall([t1,t2])


# 进程锁
import gevent
from gevent.lock import Semaphore  #锁
sem = Semaphore(1) #实例化一个锁
def fun1():
    for i in range(5):
        sem.acquire()
        print("fun 1 this is %s"%i)
        gevent.sleep(1)
        sem.release()

def fun2():
    for i in range(5):
        sem.acquire()
        print("fun 2 this is %s"%i)
        sem.release()

t1 = gevent.spawn(fun1)
t2 = gevent.spawn(fun2)

gevent.joinall([t1,t2])


