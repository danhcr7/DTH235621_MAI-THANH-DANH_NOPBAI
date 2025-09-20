s = input("Nhập Chuỗi: ")
def solve(s):
    ketqua = []
    # duyệt từ index 0 ---> n-2
    n = len(s)
    for i in range(0, n-1, 1):
    # khi nào gặp - thì dùng j quét hết, còn != - thì continue
        if (s[i] != "-"): 
            continue
        else:
            k = ""
            # dùng j quét từ s[i+1] đến s[n-1]
            for j in range(i+1, n, 1):
                if (s[j].isdigit()): k += s[j]
                else: break 
            if (k.isdigit()): ketqua.append(("-"+ k))
    for tmp in ketqua:
        print(tmp, end = " ")
solve(s)