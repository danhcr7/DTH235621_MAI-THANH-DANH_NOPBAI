# Kiểm tra tính đối xứng của chuỗi:
s = input("Nhập chuỗi: ")
tmp, k, n = 0, -1, len(s)
for i in range(0, n, 1): 
    # 0 ---> n-1
    if (s[i] == s[k]):
        tmp += 1 
    if (k+n >= 0): k -= 1 
if (tmp == n): print("Đối Xứng")
else: print("Không đối xứng")
    
        