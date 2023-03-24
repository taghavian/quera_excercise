# print(*[x for x in sorted([x for x in map(int, input().split()[5::6]) if x % 6 == 0])])

def calc(a: list) -> tuple:
    n=len(a)
    a.sort()
    ave=sum(a)/len(a)
    
    if n%2==0:
        miane=sum(a[int(n/2)-1:int(n/2)+1])/2
    else:
        miane=a[n//2]
    maxi=max(a)
    return ave,miane,maxi

calc([2,20,30,29])