# Write your code here.
from threading import Lock,Thread



n = int(input("Enter a positive integer: "))


def print_foo(n,foo_lock,bar_lock):
    for i in range(n):
        foo_lock.acquire()
        print("foo",end="")
        bar_lock.release()

def print_bar(n,bar_lock,foo_lock):
    for i in range(n):
        bar_lock.acquire()
        print("bar",end="")
        foo_lock.release()

foo_lock = Lock()
bar_lock = Lock()
bar_lock.acquire()


t1 = Thread(target=print_foo,args=(n,foo_lock,bar_lock))
t2 = Thread(target=print_bar,args=(n,bar_lock,foo_lock))

t1.start()
t2.start()

t1.join()
t2.join()