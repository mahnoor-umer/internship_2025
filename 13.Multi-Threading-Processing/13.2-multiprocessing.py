## Parallel tasks
## High computational power - Heavy load on the CPU ; Data anaysis
## Cores

import multiprocessing
import time


def square():
    for i in range(5):
        time.sleep(1)
        print( f"Square : {i * i}")

def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i * i * i}")

if __name__ == '__main__':        

    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    t = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    time_finished= time.time() - t
    print(f"Finished in {time_finished} seconds")
