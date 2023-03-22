a=input().split(' ')
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
num=int(input())
pos=[]
for i in range(num):
    b=[]
    a=input()
    a=a.split(" ")
    for q in range(len(a)):
        b.append(int(a[q]))
    pos.append(b)

for i in range(num):
    