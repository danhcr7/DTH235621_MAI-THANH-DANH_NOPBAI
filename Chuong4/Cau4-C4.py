# Viết Hàm tính ROI:
dt, cp = map(int, input().split())
def ROI(dt, cp):
    return (dt-cp)/cp
def LoiKhuyenDauTu():
    k = ROI(dt, cp)
    if (k>=0.75): print("ROI:",k, "| Lời Khuyên: Nên Đầu Tư")
    else: print("ROI:", k, "| Lời Khuyên: Không Nên Đầu Tư")
LoiKhuyenDauTu()