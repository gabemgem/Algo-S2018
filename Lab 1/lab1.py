import matplotlib.pyplot as plt
import numpy as np
import sys
import timeit

def fib1(n):
    if n==0:
        return 0
    if n==1:
        return 1
        fib1(n-1)
    return fib1(n-1)+fib1(n-2)
        
def fib2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a=0
    b=1
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    return c

##Lab 1 Part 1
'''
nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41, 42, 43]
times1 = []
times2 = []
for i in nums:
    t1 = timeit.timeit(lambda:fib1(i), number=1)
    t2 = timeit.timeit(lambda:fib2(i), number=1)
    times1.append(t1)
    times2.append(t2)
    
print ('%-4s%-12s%-12s' % ('N', 'fib1 Time', 'fib2 Time'))
for k in range(12):
    print ('%-4i%-12.7f%-12.10f' % (nums[k], times1[k], times2[k]))

        
ind = np.arange(12)
width=.35

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=False)
ax=axes[0]
ax.bar(ind, times1, width, color='r')

ax.set_xlabel('n')
ax.set_ylabel('Times')
ax.set_title('Fib1 Running Times')
ax.set_xticks(ind)
ax.set_xticklabels(nums)

ax=axes[1]

ax.bar(ind, times2, width, color='b')

ax.set_xlabel('n')
ax.set_ylabel('Times')
ax.set_title('Fib2 Running Times')
ax.set_xticks(ind)
ax.set_xticklabels(nums)

plt.show()
'''

##Lab1 Part 2

nums = [1024, 4096, 16384, 65536, 262144, 524288]
times1 = []
for i in nums:
    t1 = timeit.timeit(lambda:fib2(i), number=1)

    times1.append(t1)
    
print ('%-8s%-12s' % ('N', 'Time'))
for i in range(6):
    print ('%-8i%-12.10f' % (nums[i], times1[i]))
   
ind = np.arange(6)
width=.35

fig, ax = plt.subplots()

ax.bar(ind, times1, width, color='r')

ax.set_xlabel('n')
ax.set_ylabel('Times')
ax.set_title('Fib1 Running Times')
ax.set_xticks(ind)
ax.set_xticklabels(nums)

plt.show()
