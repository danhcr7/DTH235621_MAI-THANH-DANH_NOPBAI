# Viết Hàm Tính diện tích tam giác:
from math import *
a, b, c = map(float, input().split())
def check(a, b, c):
    if (a<=0 or b<=0 or c<=0): return False
    # a>0 và b>0 và c>0
    if (a+b<=c or a+c<=b or b+c<=a): return False
    return True
def tinhDT(a, b, c):
    if (check(a, b, c)): 
        p = (a+b+c)/2
        dt = sqrt(p*(p-a)*(p-b)*(p-c))
        return dt
    else: 
        return -1
tmp = tinhDT(a, b, c)
if (tmp>0): print("Diện tích tam giác là: %.2f" % tmp)
else: print(-1)