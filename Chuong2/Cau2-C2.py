"""
Nhập Giây xuất ra giờ phút giây
"""
s = int(input("Nhập Giây: "))
gio = s // 3600
phut = (s - 3600*gio) // 60 
giay = (s - (gio*3600 + phut*60))
print("Số Giờ:", gio, "; Số Phút:", phut, "; Số Giây:", giay)