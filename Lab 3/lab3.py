import math
import random

def modexp(x,y,n):
    if y==0:
        return 1
    z = modexp(x,math.floor(y/2),n)
    if y%2==0:
        z=z*z
        z=z%n
        return z
    else:
        z=z*z
        z=x*z
        z=z%n
        return z
    
def prim(n, k):
    t=0
    f=0
    for i in range(0,k):
        z=random.randint(1,n-1)
        if modexp(z,n-1,n) != 1:
            f=f+1
            
        else:    
            t=t+1
    print("true: "+str(t))
    print("false: "+str(f))
    
        


carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
for n in carmichael:
    print(n)
    prim(n,1000)
        
