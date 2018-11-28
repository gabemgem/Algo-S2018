import numpy

def selection(S,k):
    if len(S)==1:
        return S[0]
    v=S[numpy.random.randint(len(S))]
    SL=[]
    Sv=[]
    SR=[]
    for n in S:
        if n<v:
            SL.append(n)
        if n==v:
            Sv.append(n)
        if n>v:
            SR.append(n)
    
    if k<=len(SL):
        return selection(SL,k)
    if k>len(SL) and k<=(len(SL)+len(Sv)):
        return v
    if k>(len(SL)+len(Sv)):
        return selection(SR, k-len(SL)-len(Sv))
    

n=100
k=10
S=[]
for i in range(n):
    S.append(numpy.random.randint(n))
    

print(selection(S,k))
print(S)
print(sorted(S))