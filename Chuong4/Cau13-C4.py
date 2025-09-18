# Kiểm tra số hoàn thiện:
def soHoanThien(n):
    s = 0
    for i in range(1, n, 1):
        if (n%i == 0): s += i 
    if (s == n): return True
    return False
# Kiểm tra số thịnh vượng:
def soThinhVuong(n):
    s = 0
    for i in range(1, n, 1):
        if (n%i == 0): s += i 
    if (s > n): return True
    return False
while True:
    n = int(input()) 
    if (soHoanThien(n)): print(n, "là số hoàn thiện")
    elif (soThinhVuong(n)): print(n, "là số thịnh vượng")
    else: print(n, "không là số hoàn thiện và thịnh vượn")    