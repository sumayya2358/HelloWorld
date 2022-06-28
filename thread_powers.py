import threading

RANGE_START = 0
RANGE_END = 1000

"""
At the end of the program, this variable needs to contain all of the powers
of 2 within the interval [RANGE_START, RANGE_END).
"""
powers_of_two = set()


def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0


def find_powers_of_two(iter):
    for i in iter:
        if is_power_of_two(i) == True:
            powers_of_two.add(i)
t1 = threading.Thread(target=find_powers_of_two,args=(range(RANGE_START,600),))
t2 = threading.Thread(target=find_powers_of_two,args=(range(601,RANGE_END),))
t1.start()
t2.start()

