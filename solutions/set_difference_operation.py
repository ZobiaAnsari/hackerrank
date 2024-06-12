A,setA,B,setB = int(input()), set(map(int,input().split())), int(input()), set(map(int,input().split()))

diff = setA.difference(setB)
print(len(diff))