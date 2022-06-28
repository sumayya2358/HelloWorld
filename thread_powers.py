# Copyright © 2022 AlgoExpert LLC. All rights reserved.

import threading

RANGE_START = 0
RANGE_END = 1000


def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0


powers_of_two = set()
set_lock = threading.Lock()


def find_powers_of_two(iter):
    for x in iter:
        if is_power_of_two(x):
            set_lock.acquire()
            powers_of_two.add(x)
            set_lock.release()


thread1 = threading.Thread(target=find_powers_of_two, args=(range(RANGE_START, 250),))
thread2 = threading.Thread(target=find_powers_of_two, args=(range(250, 500),))
thread3 = threading.Thread(target=find_powers_of_two, args=(range(500, 750),))
thread4 = threading.Thread(target=find_powers_of_two, args=(range(750, RANGE_END),))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
