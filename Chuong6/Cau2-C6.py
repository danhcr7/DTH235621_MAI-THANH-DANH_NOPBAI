import random
n = int(input())
a = [random.randint(0,100) for _ in range(n)]
print(a)
# Nhập k xóa hết k 
b = []
k = int(input())
for i in a:
    if (i!=k): b.append(i)
a = b 
print(a)