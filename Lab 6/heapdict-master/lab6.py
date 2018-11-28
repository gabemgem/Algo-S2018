from heapdict import heapdict
import sys

def dijkstra(G, s, m):
    dist = [sys.maxsize for i in range(0,m+1)]
    prev = [None for i in range(0,m+1)]
    dist[s]=0
    
    H = heapdict()
    for i in range(0,m+1):
        H[i]=dist[i]
        
    
    
    while len(H)!=0:
        u=H.popitem()[0]
        
        if u in G:
            edges=G[u]
            
            for e in edges:
                if dist[e[0]]>dist[u]+e[1]:
                    dist[e[0]]=dist[u]+e[1]
                    
                    H[e[0]] = dist[u]+e[1]
                    prev[e[0]]=u
    
    for i in range(1,m+1):
        x=i
        temp=[]
        temp.append(i)        
        
        while prev[x] != None:
            x=prev[x]
            temp.append(x)
            
        temp.reverse()
        print(str(i)+": "+str(dist[i])+", "+str(temp))
        
    


f = open("rome99.txt", "r")
                
G={}

m=0
for line in f:
    temp = line.split()
    u=int(temp[0])
    v=int(temp[1])
    w=int(temp[2])
    temp2=[]
    if u in G:
        temp2=G[u]
    temp2.append((v,w))
    G[u]=temp2
    m=max([m,u,v])

dijkstra(G, 1, m)