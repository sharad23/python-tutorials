from multiprocessing import Pool
from time import sleep
def f(x):
    sleep(1)
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    # map(f, [1, 2, 3])
    p = Pool(5)
    print p.map(f, [1,2,3,4,5,6,7,8,9,10])
    print 'next'
    print p.imap_unordered(f,[1,2,3,4,5,6,7,8,9,10])
    for i in p.imap_unordered(f,[1,2,3,4,5,6,7,8,9,10]):
       print i
