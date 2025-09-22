lst = [20, 1, -34, 40, -8, 60, 1, 3]
# lst: ra list đó luôn [20, 1, -34, 40, -8, 60, 1, 3]
print(lst)
# lst[0:3] ra [20, 1, -34]
print(lst[0:3])
# lst[4:8] ra [-8, 60, 1, 3]
print(lst[4:8])
# lst[4:33] cắt tới hết
print(lst[4:33])
# lst[-5:-3] ra [40, -8]
print(lst[-5:-3])
# lst[-22:3] ra [20, 1, -34]
print(lst[-22:3])
# lst[4:] ra [-8, 60, 1, 3]
print(lst[4:])
# lst[:]: ra ban đầu
print(lst[:])
# lst[:4] ra [20, 1, -34, 40]
print(lst[:4])
# lst[1:5] ra [1, -34, 40, -8]
print(lst[1:5])
# -34 in lst: ra True
print(-34 in lst)
# -34 not in lst: ra False
print(-34 not in lst)
# len(lst) ra 8
print(len(lst))