l = []
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    x = int(input())
    # add hay nhập lại:
    test1, test2 = l.copy(), l.copy()
    test1.append(x)
    test2.append(x)
    test2.sort()
    if (test1 == test2): 
        # add trực tiếp
        l.append(x)
    else:
        # nhập lại:
        j = True
        while (j):
            x = int(input("Nhập lại x: "))
            test3, test4 = l.copy(), l.copy()
            test3.append(x)
            test4.append(x)
            test4.sort()
            if (test3 == test4): 
                l.append(x)
                j = False
print(l)
