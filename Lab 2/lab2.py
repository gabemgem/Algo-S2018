import math
import sys
import random
import timeit

def mult1(x,y):
    prod=0;
    l=y.bit_length()
    temp=x
    
    
    for i in range(0,l):
        temp=x
        temp=temp<<i
        
                
        if y&1 is 1:
            prod+=temp
        y=y>>1
        
        
    return prod


def mult2(x,y):
    if y is 0:
        return 0
    z=mult2(x,y>>1)
    if y&1 is 0:
        return z<<1
    else:
        return x+(z<<1)

def mult3(x,y):
    
    n=max(x.bit_length(),y.bit_length())
    
    if n <= 1:
        if x==1 and y==1:
            return 1
        else:
            return 0
    xl, xr, yl, yr = 0,0,0,0

    for i in range(0, math.floor(n>>1)):
        xr+=(x&1)<<i
        yr+=(y&1)<<i
        x=x>>1
        y=y>>1
    
    for j in range(0, math.ceil(n>>1)):
        xl+=(x&1)<<j
        yl+=(y&1)<<j
        x=x>>1
        y=y>>1
    
    p1 = mult3(xl,yl)
    p2 = mult3(xr,yr)
    p3 = mult3(xl+xr, yl+yr)
    
    part1 = p1<<((math.floor(n>>1))<<1)
    part2 = (p3-p1-p2)<<(math.floor(n>>1))
    return part1+part2+p2

d=int(input())             ##int(sys.argv[1])
t1avg, t2avg, t3avg = 0,0,0
for r in range(0,10):
    
    xstring, ystring, temp = "", "", 0
    temp=random.randint(1,9)
    xstring=str(temp)
    temp=random.randint(1,9)
    ystring=str(temp)
    for i in range(0,d-1):
        temp=random.randint(0,9)
        xstring=xstring+str(temp)
        temp=random.randint(0,9)
        ystring=ystring+str(temp)
    
    x=int(xstring)
    y=int(ystring)
    
    t1 = timeit.timeit(lambda:mult1(x,y), number=10)
    t2 = timeit.timeit(lambda:mult2(x,y), number=10)
    t3 = timeit.timeit(lambda:mult3(x,y), number=10)
    t1avg+=t1
    t2avg+=t2
    t3avg+=t3
    
t1avg/=10
t2avg/=10
t3avg/=10
print(t1avg)
print(t2avg)
print(t3avg)

print(mult1(10,8))
print(mult2(10,8))
print(mult3(10,8))