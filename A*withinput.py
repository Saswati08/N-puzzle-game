from queue import PriorityQueue
from functools import total_ordering
import copy
n=int(input())
t=[]
i=0
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    t.append(row)
print(t)
#print(type(t))
k=1
i=0
j=0
goal=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(k)
        k=k+1
    goal.append(row)
#print(goal)        
goal[n-1][n-1]=0 
#print(type(n))
print(goal)
q=PriorityQueue()
visited=set()
class config:
    def __init__(self, moves, heuristic, con):
        #print('jdfnjksdkf')
        self.moves=moves
        self.heuristic=heuristic
        self.con=con
        self.priority=self.heuristic
    def __lt__(self,other):
        return (self.priority<other.priority)

def flatten(t):
    flat=[]
    for i in t:
        for j in i:
            flat.append(j)
    return flat
def find0(t):
    i=0
    while(i<n):
        j=0 
        while(j<n):
            if(t[i][j]==0):
                return(i,j)
            j+=1
        i+=1
    return -1
def heu(t):
    c=0
    i=0
    while(i<n):
        j=0 
        while(j<n):
            if(t[i][j]!=goal[i][j]):
                c+=1
            j+=1
        i+=1
    #print('c is printed:',c)        
    return c


if(t==goal):
    print("Goal Reached")
else:
    h=heu(t)
    q.put(config(0,h,t))
    nw=flatten(t)
    visited.add(tuple(nw))
    i=0
    #print(q.popleft())
    while(not q.empty()):
        i+=1
        front=q.get()
        nw=flatten(front.con)
        visited.add(tuple(nw))
        #print("front is printed")
        #print(front.con)
		#print(front.priority)
        print(i)
        if(front.con==goal):
            print(front.con)
            print("Goal Reached")
            break
    	        
        else:
            index1,index2=find0(front.con)
            #print(index1)
            #print(index2)
                
            if(index1<n-1 ):
                g=copy.deepcopy(front.con)
                g[index1][index2],g[index1+1][index2]=g[index1+1][index2],g[index1][index2]
                nw=tuple(flatten(g))
                if(nw not in visited):
                    h=heu(g)
                    q.put(config(front.moves+1,h,g))
                    visited.add(nw)
                    #print("g is printed")
                    #print(g)
                    
            if(index1>=1 ):
                f=copy.deepcopy(front.con)
                f[index1][index2],f[index1-1][index2]=f[index1-1][index2],f[index1][index2]
                nw=tuple(flatten(f))
                if(nw not in visited):
                    h=heu(f)
                    q.put(config(front.moves+1,h,f))
                    visited.add(nw)
    		        #print("f is printed")
    		        #print(f)
                    
                
            if(index2<n-1 ):
                l=copy.deepcopy(front.con)
                l[index1][index2],l[index1][index2+1]=l[index1][index2+1],l[index1][index2]
                nw=tuple(flatten(l))
                if(nw not in visited):
                    h=heu(l)
                    q.put(config(front.moves+1,h,l))
                    visited.add(nw)
    			    #print("l is printed")
    			    #print(l)
                    
                
            if(index2>=1 ):
                z=copy.deepcopy(front.con)
                z[index1][index2],z[index1][index2-1]=z[index1][index2-1],z[index1][index2]
                nw=tuple(flatten(z))
                if(nw not in visited):
                    h=heu(z)
                    q.put(config(front.moves+1,h,z))
                    visited.add(nw)
    			    #print("n is printed")
    			    #print(n)
    print(i)        
                