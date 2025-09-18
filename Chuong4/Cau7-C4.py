# tính độ dài AB
from math import *
xa, xb, ya, yb = map(float, input().split())
def dodaiAB(xa, xb, ya, yb):
   dodai =  sqrt(pow(xb-xa, 2)+pow(yb-ya, 2))
   return dodai
dodai = dodaiAB(xa, xb, ya, yb)
print("Độ dài đoạn thẳng AB la: %.3f" % dodai)