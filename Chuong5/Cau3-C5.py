# Xử Lý Tách Chuỗi:
# Nhập chuỗi theo định dạng: “5;7;8;-2;8;11;13;9;10”
s = input("Nhập chuỗi: ")
# Yêu cầu 1: Xuất các chữ số trên dòng riêng biệt
def yeucau1(s):
    print("# Thực hiện yêu cầu 1")
    my_list = s.split(';')
    for i in my_list:
        print(i, end = "\n")
yeucau1(s)
# Yêu cầu 2: Xuất ra có bao nhiêu chữ số chẵn:
def yeucau2(s):
    print("# Thực hiện yêu cầu 2")
    my_list = s.split(';')
    s = 0
    for i in my_list:
        j = int(i)
        if (j%2 == 0): s += 1
    return s
ketQua2 = yeucau2(s)
print("Số lượng số chẵn là:", ketQua2)
# Yêu cầu 3: Xuất ra có bao nhiêu số âm:
def yeucau3(s):
    print("# Thực hiện yêu cầu 3")
    my_list = s.split(';')
    s = 0
    for i in my_list:
        j = int(i)
        if (j < 0): s += 1
    return s
ketQua3 = yeucau3(s)
print("Số lượng số âm là:", ketQua3)
# Yêu cầu 4: Có bao nhiêu chữ số nguyên tố:
def check_snt(x):
    if (x<2): return False
    s = 0
    for i in range(1, x+1, 1):
        if (x%i == 0): s += 1
    if (s>2): return False
    return True
def yeucau4(s):
    sum = 0
    print("# Thực hiện yêu cầu 4")
    my_list = s.split(';')
    for i in my_list:
        j = int(i)
        if (check_snt(j)): sum += 1
    return sum
ketQua4 = yeucau4(s)
print("Số lượng số nguyên tố là:", ketQua4)

# Yêu cầu 5: Tính giá trị trung bình
def yeucau5(s):
    sum = 0
    print("# Thực hiện yêu cầu 5")
    my_list = s.split(';')
    for i in my_list:
        j = int(i)
        sum += j
    return (sum/len(my_list))
ketQua5 = yeucau5(s)
print("Giá trị trung bình là:", ketQua5)