s = input()
def sx_giam(s):
    s1 = s.strip()  
    my_list_0, my_list_1 = s1.split(), []
    for i in my_list_0:
      j = int(i)
      my_list_1.append(j)
    my_list_1.sort(reverse = True)
    kq = ""
    for i in my_list_1:
        kq += (str(i) + " ")
    return kq.strip()
k = sx_giam(s)
print(k)