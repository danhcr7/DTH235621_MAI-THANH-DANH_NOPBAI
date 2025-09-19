# Tối ưu chuỗi:
def toiUuChuoi(s):
    kq = ""
    a = s.strip()
    my_list = a.split()
    for i in my_list:
        kq += (i + " ")
    return kq.strip()
s = input("Nhập chuỗi: ")
print("Chuỗi được tối ưu là:", toiUuChuoi(s))      