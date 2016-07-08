from multiprocessing import Process
from time import sleep
import os

def f(x):
    sleep(2)
    print x
    return x*x

if __name__ == '__main__':
    p = Process(target=f, args=(1,))
    p.start()
    #p.join()
    q = Process(target=f, args=(2,))
    q.start()
    #q.join()
    s = Process(target=f, args=(3,))
    s.start()
    #s.join()
