import time
from collections import deque
import copy
goal=[]
start=time.time()
def find0(t,n):
    i=0
    while(i<n):
        j=0
        while(j<n):
            if(t[i][j]==0):
                return(i,j)
            j=j+1
        i=i+1
    return -1
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
for i in range(n):
    row=[]
    for j in range(n):
        row.append(k)
        k=k+1
    goal.append(row)
goal[n-1][n-1]=0
print(goal)
q=deque()
visited=set()
if(t==goal):
    print("Goal Reached")
    end=time.time()
    print(end-start)
    print(1)
    print(0)
    exit()
else:
    q.append(t)
    i=0
    max=0
    while(len(q)!=0):
        i=i+1
        front=q.popleft()
        #print(front)
        nw=sum(front,[])
        visited.add(tuple(nw))
        index1,index2=find0(front,n)
        #print(index1)
        #print(index2)
        if(index1<n-1):
            g=copy.deepcopy(front)
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
                nw=tuple(sum(g,[]))
                if( nw not in visited):
                    visited.add(nw)
                    q.append(g)
                    if(max<len(q)):
                        max=len(q)
                    #print("g is printed")
                    #print(g)
        if(index1>=1):
            f=copy.deepcopy(front)
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
                nw=tuple(sum(f,[]))
                if( nw not in visited):
                    visited.add(nw)
                    q.append(f)
                    if(max<len(q)):
                        max=len(q)
                    #print("fis printed")
                    #print(f)
        if(index2<n-1):
            l=copy.deepcopy(front)
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
                nw=tuple(sum(l,[]))
                if( nw not in visited):
                    visited.add(nw)
                    #print("l is printed")
                    q.append(l)
                    if(max<len(q)):
                        max=len(q)
                    #print(l)
        if(index2>=1):
            x=copy.deepcopy(front)
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
                nw=tuple(sum(x,[]))
                if( nw not in visited):
                    visited.add(nw)
                    q.append(x)
                    if(max<len(q)):
                        max=len(q)
                    #print("n is printed")
                    #print(x)
    print(i)



