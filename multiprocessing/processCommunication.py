from multiprocessing import Process, Pipe
from time import sleep

def write(conn):
    
    sleep(1)
    conn.send([42, None, 'hello'])
    conn.close()

def read(conn):
    
    print conn.recv()
    conn.close()
    

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=write, args=(child_conn,))
    p.start()
    q = Process(target=read, args=(parent_conn,))
    q.start()
    p.join()
    q.join()
    
