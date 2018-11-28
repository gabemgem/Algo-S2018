import sys


def dist(x, y):
    xprime = x
    yprime = y

    E = []
    for b in range(0, len(x)+1):
        temp = []
        for a in range(0, len(y)+1):
            temp.append(0)        
        E.append(temp)

    for i in range(0, len(x)+1):
        E[i][0] = i
        
    

    for j in range(1, len(y)+1):
        E[0][j] = j
        
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            E[i][j] = min({E[i-1][j]+1, E[i][j-1]+1, E[i-1][j-1]+diff(x,y,i-1,j-1)})

    xprime, yprime = path(E, x, y)
    
    return E[len(x)][len(y)], xprime, yprime

def path(E, x, y):
    i = len(E)-1
    j = len(E[0])-1
    stop = False
    while stop is not True:
        if i==0:
            j=j-1
            x = insert(x, 0)
        elif j==0:
            i=i-1
            y = insert(y, 0)
        else:
            m = min({E[i][j-1], E[i-1][j], E[i-1][j-1]})
            if E[i-1][j-1] is m:
                i=i-1
                j=j-1
                continue
            elif E[i][j-1] is m:
                j=j-1
                x = insert(x, i)
            else:
                i=i-1
                y = insert(y, j)
                
        if i<=0:
            if j<=0:
                stop=True
                
    return x, y
                
def plist(E):
    for i in range(0, len(E)):
        print(E[i])

def diff(x,y,i,j):
    if x[i] is y[j]:
        return 0
    return 1

def insert(s,i):
    temp1 = s[0:i]
    temp2 = s[i:len(s)+1]
    s=temp1 + "-" + temp2
    return s


debug = 0

if debug is 1:
    X = "EXPONENTIAL"
    Y = "POLYNOMIAL"
else:
    X = "CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG"
    Y = "CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA"
    
d, x, y = dist(X, Y)
print("edit distance = " + str(d))
print("alignment:")
print(x)
print(y)

