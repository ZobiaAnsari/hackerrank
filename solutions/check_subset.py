TC=int(input())
for i in range(TC):
    A,setA,B,setB=int(input()),set(map(int,input().split())),int(input()),set(map(int,input().split()))
  
    if setA.issubset(setB):
        print(True)
    else:
        print(False)