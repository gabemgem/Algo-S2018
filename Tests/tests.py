import math

def exp(x,y):
    if y is 0: return 1
    if y is 1: return x
    i=2
    temp=x
    x=x*x
    
    while i*i < y:
        x=x*x
        i=i*i
    while i < y:
        x=x*temp
        i=i+1
    return x

print(exp(9,7))