from queue import Queue

def main():
    q = Queue()
    l_o_n = [i for i in range(1,11)]
    fill_q( q, l_o_n)
    print_q(q)
    print("---------------")
    pop_list(l_o_n)
    print("---------------")

    print(l_o_n)
    

def pop_list(l_o_n):
    print(l_o_n.pop())
    

def fill_q( q, l_o_n):
    for i in l_o_n:
        q.put(i)

def print_q(q):
    while not(q.empty()):
        print(q.get())
    


main()
