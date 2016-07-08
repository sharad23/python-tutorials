# Bucket simulation
from  multiprocessing import Process,Queue
import time
import random


def fill_the_bucket(data):

    while True:
        #insert  value in the list
        time.sleep(5)
        val = random.randrange(10,1000)
        print "random value"
        print val
        data.put(val)
        print "container after push"
        print data


def empty_the_bucket(data):

    while True:

        # empty the bucket
        time.sleep(10)
        if not data:
           print "empty"
           print  data

        else:
             element = data.get()
             print "conatiner after pop"
             print element
             # process this signal

if __name__ == '__main__':
    print "Begin execution..................."
    s = Queue()
    p = Process(target=fill_the_bucket,args=(s,))
    p.start()
    q = Process(target=empty_the_bucket,args=(s,))
    q.start()
    p.join()
    q.join()




# from multiprocessing import Process
# from time import sleep
# import os
#
# def f(x):
#     sleep(2)
#     print x
#     return x*x
#
# if __name__ == '__main__':
#     p = Process(target=f, args=(1,))
#     p.start()
#     #p.join()
#     q = Process(target=f, args=(2,))
#     q.start()
#     #q.join()
#     s = Process(target=f, args=(3,))
#     s.start()
#     #s.join()
#     #print "ok"
#     # p.join()
#     # q.join()
#     # s.join()




# from multiprocessing import Process, Value, Array,Queue
# from time import sleep
#
# def f(n, a):
#     sleep(4)
#     n.value = 3.1415927
#     for i in range(5):
#         a.put(i)
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Queue()
#     p = Process(target=f, args=(num, arr))
#     p.start()
#     print num.value
#     print arr
#     # p.join()
#     print num.value
#     print arr

#
# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put(10)
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print q.get()    # prints "[42, None, 'hello']"
#     p.join()
