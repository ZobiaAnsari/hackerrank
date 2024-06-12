import re

TC = int(input())
for i in range(TC):
    string = input()
    try:
        if re.compile(string):
            print(True)
    except:
        print(False)