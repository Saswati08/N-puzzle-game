import time
from queue import PriorityQueue
from functools import total_ordering
import copy
start=time.time()
n=int(input())
t=[]
i=0
for i in range(n):
    row=input().split()
    for i in range(len(row)):
        row[i]=int(row[i])
    t.append(row)
print(t)
k=1
i=0
j=0
goal=[]
for i in range(n):
    row=[]
    for  j in range(n):
        row.append(k)
        k=k+1
    goal.append(row)
goal[n-1][n-1]=0
print(goal)
class config:
    def __init__(self,moves,heuristic,con):
        self.moves=moves
        self.heuristic=heuristic
        self.con=con
        self.priority=self.heuristic
    def __lt__(self,other):
        return (self.priority<other.priority)
def find0(t):
    i=0
    while(i<n):
        j=0
        while(j<n):
            if(t[i][j]==0):
                return (i,j)
            j=j+1
        i+=1
    return -1
def heu(t):
    c=0
    i=0
    while(i<n):
        j=0
        while(j<n):
            if(t[i][j]!=goal[i][j]):
                c=c+1
            j+=1
        i+=1
    return c
q=PriorityQueue()
if(t==goal):
    print("Goal Reached")
    end=time.time()
    print(end-start)
    print(1)
    print(0)
    exit()
else:
    limit=2
    h=heu(t)
    visited=set()
    
    nw=tuple(sum(t,[]))
    if(nw not in visited):
        visited.add(nw)
        q.put(config(0,h,t))
    i=0
    max=0
    while(True):
        i=i+1
        #print(limit)
        visited=set()
        q.put(config(0,h,t))
        nw=tuple(sum(t,[]))
        visited.add(nw)
        while(not q.empty()):
            
            front=q.get()
            #print(front)
            nw=sum(front.con,[])
            visited.add(tuple(nw))
            index1,index2=find0(front.con)
            #print(index1)
            #print(index2)
            if(index1<n-1):
                g=copy.deepcopy(front.con)
                g[index1][index2],g[index1+1][index2]=g[index1+1][index2],g[index1][index2]
                if(goal==g):
                    print("Goal Reached")
                    print(g)
                    end=time.time()
                    print(end-start)
                    print(i)
                    print(max)
                    exit()
                else:
                    h=heu(g)
                    nw=tuple(sum(g,[]))
                    if( nw not in visited and h<=limit):
                        visited.add(nw)
                        q.put(config(front.moves+1,h,g))
                        if(max<q.qsize()):
                            max=q.qsize()
                        #print("g is printed")
                        #print(g)
            if(index1 > 0):                  
                f =copy.deepcopy(front.con)
                f[index1][index2],f[index1-1][index2]=f[index1-1][index2],f[index1][index2]
                if(goal==f):
                    print("Goal Reached")
                    print(f)
                    end=time.time()
                    print(end-start)
                    print(i)
                    print(max)
                    exit()
                else:
                    h=heu(f)
                    nw=tuple(sum(f,[]))
                    if( nw not in visited and h<=limit):
                        visited.add(nw)
                        q.put(config(front.moves+1,h,f))
                        #print("fis printed")
                        #print(f)
                        if(max<q.qsize()):
                            max=q.qsize()
                        #print(limit)
            if(index2<n-1):
                l=copy.deepcopy(front.con)
                #print("here?")
                l[index1][index2],l[index1][index2+1]=l[index1][index2+1],l[index1][index2]
                #print(l)
                if(goal==l):
                    #print("not here?")
                    print("Goal Reached")
                    print(l)
                    end=time.time()
                    print(end-start)
                    print(i)
                    print(max)
                    exit()
                else:
                    h=heu(l)
                    nw=tuple(sum(l,[]))
                    if( nw not in visited and h<=limit):
                        visited.add(nw)
                        #print("l is printed")
                        if(max<q.qsize()):
                            max=q.qsize()
                        q.put(config(front.moves+1,h,l))
                        #print(l)
            if(index2>=1):
                x=copy.deepcopy(front.con)
                x[index1][index2],x[index1][index2-1]=x[index1][index2-1],x[index1][index2]
                if(goal==x):
                    print("Goal Reached")
                    print(x)
                    end=time.time()
                    print(end-start)
                    print(i)
                    print(max)
                    exit()
                else:
                    h=heu(x)
                    nw=tuple(sum(x,[]))
                    if( nw not in visited and h<=limit):
                        visited.add(nw)
                        q.put(config(front.moves+1,h,x))
                        if(max<q.qsize()):
                            max=q.qsize()
                        #print("n is printed")
                        #print(x)
        limit+=2
        #print(limit)
