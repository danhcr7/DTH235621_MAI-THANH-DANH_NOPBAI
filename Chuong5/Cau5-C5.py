s = input("Nhập chuỗi: ")
def check(s):
    tonghoa, tongthuong, tongso, db, kt, na, n = 0, 0, 0, 0, 0, 0, len(s)
    for i in range(0, n):
        if (s[i].isupper()): tonghoa += 1 
        if (s[i].islower()): tongthuong += 1
        if (s[i].isdigit()): tongso += 1
        if (s[i].isalpha()==False and s[i].isdigit()==False): db += 1
        if (s[i] == " "): kt += 1
        if (s[i]=="a" or s[i]=="o" or s[i]=="e" or s[i]=="u" or s[i]=="i"): na += 1
    return f"""Số lượng chữ cái hoa: {tonghoa};
Số lượng chữ cái thường: {tongthuong};
Số lượng kí tự là số: {tongso};
Số lượng kí tự đặc biệt: {db};
Số lượng kí tự là khoảng trắng là: {kt}
Số lượng kí tự là nguyên âm: {na}
Số lượng kí tự là phụ âm: {n-na}"""
print(check(s))     


