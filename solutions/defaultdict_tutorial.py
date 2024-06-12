from collections import defaultdict

n,m = map(int,input().split())

d=defaultdict(list)
for i in range(n):
    ele = input()
    d[ele].append(i+1)

for i in range(m):
    ele = input()
    
    if ele in d:
        print(' '.join(map(str,d[ele])))
    else:
        print(-1)