## Programme : Sequence of code
## Process   : Instance of a programme
## Thread    : Unit of execution

## 1.Code segment , 2.Heap , 3.Data segment
## 4.Stack , 5.Registers
## 6.Thread

## File operations / I/O -> concurently


import threading
import time

def print_letters():
    for letter in 'abcd':
        time.sleep(2)
        print(f'Letter: {letter}')

def print_LETTERS():
    for letter in 'ABCD':
        time.sleep(2)
        print(f'Letter: {letter}')

t1= threading.Thread(target= print_letters)  
t2= threading.Thread(target= print_LETTERS)

t = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

time_finished= time.time()-t

print(time_finished)