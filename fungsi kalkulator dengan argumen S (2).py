L=[1, 2, 3, 4, 5]
s=[]
for i in L:
    s.append(i*2)
    
s=list(map(lambda x : x*2, L))
g=list(filter(lambda x : x % 2, L))

g=[]
for i in L:
    if i % 2:
        g.append(i)
        
