# Viết Hàm Tính BMI:
m, h = map(float, input().split())
def BMI(m, h):
    BMI = m/(h*h)
    return BMI
chi_so_BMI = BMI(m, h)
def phanLoai():
    if (chi_so_BMI<18.5): 
        return "Gầy | Nguy cơ phát triển bệnh thấp"
    elif (18.5<=chi_so_BMI and chi_so_BMI<=24.9):
        return "Bình Thường | Nguy cơ phát triển bệnh trung bình"
    elif (25.0<=chi_so_BMI and chi_so_BMI<=29.9):
        return "Hơi Béo | Nguy cơ phát triển bệnh cao"
    elif (30.0<=chi_so_BMI and chi_so_BMI<=34.9):
        return "Béo Phì Cấp 1 | Nguy cơ phát triển bệnh cao"
    elif (35.0<=chi_so_BMI and chi_so_BMI<=39.9):
        return "Béo Phì Cấp 2 | Nguy cơ phát triển bệnh rất cao" 
    elif (40.0<=chi_so_BMI):
        return "Béo Phì Cấp 3 | Nguy cơ phát triển bệnh nguy hiểm"
print(phanLoai())