from collections import defaultdict
from copy import deepcopy
t = input()

def test(q,n,s,p,d,res):
    if n <= 0:
        return res
    cur = q[-1]
    index = d[cur].pop(0)
    if not d[cur]:
        del d[cur]
        q.pop()
    p[index] = -1

    # define other return var
    d1 = deepcopy(d)
    n1 = n
    p1 = deepcopy(p)
    q1 = deepcopy(q)

    if index == s-1:
        if p[index-1] != -1:
            big = index-1
        else:
            big = False
    elif index == 0:
        if p[1] != -1:
            big = 1
        else:
            big = False
    elif p[index-1]<=p[index+1]:
        if p[index+1] != -1:
            big = index+1
        else:
            big = False
    else:
        big = index-1
    if big and p[big] != -1:
        #remove if free exist
        n -= 1
        d[p[big]].remove(big)
        if not d[p[big]]:
            del d[p[big]]
            q.pop()
        p[big] = -1
    res += cur
    n -= 1
    n1 -= 1
    if big or p[big] != -1:
        return min(test(q,n,s,p,d,res),test(q1,n1,s,p1,d1,res))
    else:
        return test(q1,n1,s,p1,d1,res)

for x in range(int(t)):
    ls = input()
    p = input()
    ls = ls.split(" ")
    s = int(ls[0])
    n = int(ls[1])
    p = p.split(" ")
    p = [int(r) for r in p]
    res = 0
    d = defaultdict(list)
    for index, num in enumerate(p):
        d[num].append(index)
    q = list(d)
    q.sort(reverse = True)
    summ = test(q,n,s,p,d,res)
    print("Case {}: {}".format(x+1,summ))

