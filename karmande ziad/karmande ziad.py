# n = int(input())
# d = dict()
# for i in range(n):
#     fname = input().split()[0]
#     d[fname] = d.get(fname, 0) + 1 
# print(max(d.values()))

n=int(input())

names=[]
for i in range(n):
    names.append(input().split(" ")[0])
rep=[]
for i in range(n):
    rep.append(names.count(names[i]))

print(max(rep))