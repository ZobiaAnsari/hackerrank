no_of_eng = int(input())
Eng=set(map(int, input().split()))
no_of_frn = int(input())
Frn=set(map(int, input().split()))
res = Eng.symmetric_difference(Frn)
print(len(res))