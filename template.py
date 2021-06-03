from collections import defaultdict
import sys
import io
import time

# Sample Input
Input = u'''\

'''
sys.stdin = io.StringIO(Input)
Start = time.time()


# Source Code

N = input()
N = int(input())
A, B, C = input().split()
A, B, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


# Exec Time
End = time.time()
Exec = End - Start
print(f'{int(Exec * 1000)} ms')
