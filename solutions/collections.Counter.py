from collections import Counter
no_shoes = int(input())
shoes_size=list(map(int,input().split(' ')))
no_customer=int(input())
Dict= Counter(shoes_size)
profit=0
for cust in range(no_customer):
    size,price =map(int,input().split(' '))
    if Dict[size]:
        Dict[size]-=1
        profit+=price
print(profit)