s = input("Nhập đường dẫn: ")
def tach_ra(s):
    n = len(s)
    tmp0 = ""
    for i in range(-1, -n-1, -1):
        if (s[i] == "/"): break
        else: tmp0 += s[i]
    tmp1 = tmp0[::-1]
    mylist = tmp1.split(".")
    return mylist[0] + " " + mylist[0] + mylist[1]
print(tach_ra(s))