import numpy
import sys

def explore(G, v, visited, pre, post, order, clock):
    visited[v]=True
    previsit(v, pre, clock)
    
    if v in G:
        temp=G[v]
        for i in temp:
            if visited[i]==False:
                explore(G, i, visited, pre, post, order, clock)
    postvisit(v, post, order, clock)
    

def dfs1(G,m,order):
    clock=[1,]
    visited=[]
    pre=[]
    post=[]
    for i in range(m+1):
        visited.append(False)
        pre.append(False)
        post.append(False)
    
    
    for i in G.keys():
        if visited[i]==False:
            explore(G, i, visited, pre, post, order, clock)

def previsit(v, pre, clock):
    pre[v]=clock[0]
    clock[0]=clock[0]+1
    
def postvisit(v, post, order, clock):
    post[v]=clock[0]
    clock[0]=clock[0]+1
    order.append(v)
    
def explore2(G, v, visited):
    visited[v]=True
    print(str(v)+" ", end="")
    
    if v in G:
        for i in G[v]:
            if visited[i]==False:
                explore2(G, i, visited)
    
def dfs2(G,m,order):
    visited=[]
    for i in range(m+1):
        visited.append(False)
    
    for i in range(len(order)):
        if visited[order[len(order)-1-i]]==False:
            
            explore2(G, order[len(order)-1-i], visited)
            print()
    

sys.setrecursionlimit(1000)
f = open("test.txt", "r")

G={}
GR={}
m=0
for line in f:
    temp = line.split()
    k=int(temp[1])
    v=int(temp[0])
    temp2=[]
    if v in G:
        temp2=G[v]
    temp2.append(k)
    G[v]=temp2
    temp2=[]
    if k in GR:
        temp2=GR[k]
    temp2.append(v)
    GR[k]=temp2    
    m=max([m,k,v])
    

order=[]



dfs1(GR,m,order)
dfs2(G,m,order)


f.close()