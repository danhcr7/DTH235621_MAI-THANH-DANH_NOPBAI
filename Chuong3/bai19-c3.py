from math import *
s = 0
x, n = map(int, input().split())
k = 2*n + 1 
for i in range(1, k+1, 2):
    s += (factorial(x)/factorial(i))
print("s =", s)
