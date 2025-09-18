"""
Nhập Điểm 3 môn: Toán; Lí; Hóa ===> Xuất ra điểm TB với 2 chữ số thập phân
"""
a, b, c = map(float, input().split())
tb = (a + b + c)/3
print("Điểm TB: %.2f" % tb)