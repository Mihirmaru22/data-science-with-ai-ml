## multi threading 
## when to use multi threading
## I/O bound tasks : tasks that spend a lot of time waiting for external resources, such as file I/O, network I/O, or database queries.
## councurrt execution : multiple threads can run simultaneously, allowing for better utilization of system resources and improved performance.

import threading 
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'number: {i}')

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')

# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
# start the threads
t1.start()
t2.start()

# wait for both threads to finish
t1.join()
t2.join()
finished_time = time.time()-t
print(f'Time taken without threading: {finished_time}') 
