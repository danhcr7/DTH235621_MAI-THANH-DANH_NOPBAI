l = []
n = int(input(" Nhập số phần tử của list: "))
for i in range(n):
    x = int(input())
    if (x not in l): l.append(x)
    else: 
        j = True
        while (j):
            x = int(input("- Nhập lại: "))
            if (x not in l): j = False
print(l)