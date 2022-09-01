from queue import Queue
import time
import threading

def main():
    q = Queue()
    l_o_n = [i for i in range(1,11)]
    fill_q( q, l_o_n)

    # create threads
    threads = []
        
    for i in range(0,10):
        t = threading.Thread(target=download_q, args=[q])
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def pop_list(l_o_n):
    print(l_o_n.pop())
    

def fill_q( q, l_o_n):
    for i in l_o_n:
        q.put(i)

def download_q(q):
    while not(q.empty()):
        item = q.get()
        print("downloading: " + str(item))
        time.sleep(int(item))
        print("downloaded: " + str(item))

        

main()
