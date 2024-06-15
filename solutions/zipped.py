n,x = map(int, input().split())
marks=[]
for i in range(x):
    marks.append(list(map(float,input().split())))
record = list(zip(*marks))
for i in record:
    tmp=(sum(i)/len(i))
    print(tmp)