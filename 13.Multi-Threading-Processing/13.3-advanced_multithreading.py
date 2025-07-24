

from concurrent.futures import ThreadPoolExecutor
import time

number = [1,2,3,4,5]
def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

t = time.time() 

with ThreadPoolExecutor(max_workers=3) as executor:
    results= executor.map(print_number,number)

for result in results:
    print(result)

time_finished= time.time()-t 
print(time_finished)
