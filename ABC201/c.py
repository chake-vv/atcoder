from collections import defaultdict
import sys
import io
import time

# Sample Input
Input = u'''\
ooo???xxxx
'''
sys.stdin = io.StringIO(Input)
Start = time.time()


# Source Code

S = input()
ans = 0
for i in range(10000):
    i_zero = str(i).zfill(4)
    flag = [False]*10
    now = i
    for j in range(4):
        flag[now % 10] = True
        now //= 10
    flag2 = True
    for k in range(10):
        if S[k] == 'o' and not flag[k]:
            flag2 = False
        if S[k] == 'x' and flag[k]:
            flag2 = False
    ans += flag2
print(ans)


# Exec Time
End = time.time()
Exec = End - Start
print(f'{int(Exec * 1000)} ms')
