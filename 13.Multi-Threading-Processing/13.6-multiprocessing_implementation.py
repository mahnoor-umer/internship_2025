## Computing factorial for some large numbers

import multiprocessing
import math
import sys
import time

## set int max str digits -> for large numbers

sys.set_int_max_str_digits(100000)

## Define a function to compute factorial

def compute_factorial(number):
    print(f" The factorial of {number} is being computed")
    result = math.factorial(number)
    print(f"The factorial of {number} is {result}")
    return result

## start time

start_time = time.time()

## multiprocessing

if __name__ == "__main__":

    numbers= [5000, 6000, 7000, 8000]

    ## Pool of worker processes

    with multiprocessing.Pool() as pool:
        results= pool.map(compute_factorial, numbers)

    
    end_time = time.time() - start_time

    print(f"Results: {results}")
    print(end_time)