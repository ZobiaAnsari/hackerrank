n = int(input())
s = set(map(int, input().split()))
no_cmd= int(input())
for cmds in range(no_cmd):
    cmd=input().split()
    if cmd[0]=='pop':
        s.pop()
    if cmd[0]=='remove':
        s.remove(int(cmd[1]))
    if cmd[0]=='discard':
        s.discard(int(cmd[1]))
    
l=list(s)
print(sum(l))