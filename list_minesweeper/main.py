def adjacency(dim,pos):
    adj=[]
    I=[-1,0,1]
    J=[-1,0,1]
    for i in I:
        for j in J:
            if (pos[0]+i>=0 and pos[1]+j>=0) and (pos[0]+i<=dim[0] and pos[1]+j<=dim[1]) and not(i==0 and j==0):
                adj.append([pos[0]+i,pos[1]+j])
    return adj

a=input().split(' ')
b=[]
for i in range(len(a)):
    b.append(int(a[i])-1)
num=int(input())
pos=[]
for i in range(num):
    c=[]
    a=input()
    a=a.split(" ")
    for q in range(len(a)):
        c.append(int(a[q])-1)
    pos.append(c)
    mine=[]
for i in range(b[0]+1):
    mine.append([])
    for j in range(b[1]+1):
        mine[i].append(0)

for i in range(num):
    adj=adjacency(b,pos[i])
    mine[pos[i][0]][pos[i][1]]='*'
    for adjacent in adj:
        if  adjacent not in pos:
            mine[adjacent[0]][adjacent[1]]+=1

for i in range(len(mine)):
    for j in range(len(mine[0])):
        print(mine[i][j]," ",end='')
    print("")