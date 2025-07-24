

from concurrent.futures import ProcessPoolExecutor
import time

x = [1,2,3,4,5,6,7]
def square(x):
    time.sleep(1)
    return x * x

t = time.time()
if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, x)

    for result in results:
        print(result)

time_finished = time.time()-t
print(f"Time taken: {time_finished} seconds")
