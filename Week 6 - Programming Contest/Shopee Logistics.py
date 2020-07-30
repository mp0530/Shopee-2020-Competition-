from collections import defaultdict
import heapq as hq
number = int(input())
d = defaultdict(list)
for i in range(number-1):
    x, y, dist = input().split(" ")
    x, y, dist = int(x), int(y), int(dist)
    d[x].append((y,dist))
    d[y].append((x,dist))
visited = set()
heap = []
def dfs(node,value,cur_visited):
    for i in d[node]:
        if i[0] not in visited and i[0] not in cur_visited:
            heap.append(value-i[1])
            dfs(i[0],value-i[1],cur_visited|{i[0]})
for i in d:
    if len(d[i]) == 1:
        if d[i][0][0] not in visited:
            dfs(d[i][0][0],-d[i][0][1],{i,d[i][0][0]})
        visited.add(i)

print(-hq.nsmallest(1,heap)[0])