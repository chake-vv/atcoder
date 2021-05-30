from collections import defaultdict
import sys
import io
import time

# Sample Input
Input = u'''\
3
2 3 3
1 3 3
1 1 1
'''
sys.stdin = io.StringIO(Input)
Start = time.time()

# Source Code

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


D = defaultdict(int)
for i in range(N):
    index = C[i] - 1
    D[B[index]] += 1

ans = 0
for j in range(N):
    if A[j] in D.keys():
        ans += D[A[j]]

print(ans)
# Exec Time
End = time.time()
Exec = End - Start
print(f'{int(Exec * 1000)} ms')
