from re import *
def solve(path):
    s=0
    with open(path, "r") as f:
        for i in f:
            if i.strip()!="":
                if not match("^#",i.strip()):
                    s+=1
    return s
print(solve("a.txt"))