x, y, z = 3, 5, 7
"""
x == 3 : True
x < y : True (vì 3 < 5)
x >= y : False (vì 3 >= 5)
x <= y : True (vì 3 <= 5)
x != y-2 : False (vì 3 = 5-2)
x < 10: True (vì 3 < 10)
x >= 0 và x < 10: True (vì 0 <= x=3 < 10)
x < 0 và x < 10: False (vì 3 < 0 là sai ---> cả mệnh đề and sai)
x >= 0 và x < 2: False (vì 3 < 2 là sai ---> cả mệnh đề and sai)
x < 0 hoặc x < 10: True (vì 3 < 10 là đúng ----> cả mệnh đề or đúng)
"""
print(x == 3)
print(x < y)
print(x >= y)
print(x <= y)
print(x != y-2)
print(x < 10)
print((x>=0) and (x<10))
print((x<0) and (x<10))
print((x>=0) and (x<2))
print((x<0) or (x<10))

