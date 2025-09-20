s = input("Nhập chuỗi: ")
def toiUuChuoi(s):
    ketQua = ""
    s1 = s.strip()
    ml = s1.split()
    for i in ml:
        ketQua += (i + " ")
    return ketQua.strip()
print(toiUuChuoi(s))