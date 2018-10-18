# $ python3 -m timeit '"-".join(str(n) for n in range(100))'
import time

a = []

# a = a + [i]
start_time = time.time()

for i in range(100000):
    a = a + [i]
    
print(time.time() -  start_time)
    
# augmented assigment +=
a = []

start_time = time.time()

for i in range(100000):
    a += [i]
    
print(time.time() -  start_time)

    
# append operation
a = []

start_time = time.time()

for i in range(100000):
    a += [i]
    
print(time.time() -  start_time)

# Results in order
# 39.46293234825134
# 0.020026445388793945
# 0.019957780838012695