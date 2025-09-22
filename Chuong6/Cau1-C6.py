# Hàm check số nguyên tố:
def nguyenTo(n):
    if (n<2): return False
    tong = 0
    for i in range(1, n+1):
        if (n%i == 0): tong += 1 
    if (tong != 2): return False
    return True
# Khởi tạo list:
a = []
# Thêm phần tử vào list:
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    x = int(input())
    a.append(x)
print(a)
# Nhập k, kiểm tra k xuất hiện trong list bao nhiêu lần:
k = int(input())
solan_k = a.count(k)
print(f"Số lần mà {k} xuất hiện: {solan_k}")
# Tổng các số nguyên tố trong list:
sum_nt = 0
for i in a:
    if (nguyenTo(i)): sum_nt += i 
print("Tổng các số nguyên tố trong list là:", sum_nt)
# Sắp xếp list:
a.sort()
print("List sau khi sắp xếp:", a)
# Xóa list:
a.clear()
print("List sau khi được xóa:", a)
