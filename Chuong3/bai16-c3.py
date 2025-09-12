for a in range(20, 100, 5):
    print("*", end = ' ')
print()
'''Có bao nhiêu dấu sao in ra màn hình'''

'''
# Giải: 
Hàm range(20, 100, 5) có start = 20; stop = 100; step = 5 sinh ra dãy số [20 25 30 ...95]
Mà: Mỗi khi a nhận 1 giá trị từ hàm range() thì in ra 1 dấu *
Do: có 16 giá trị mà hàm range sinh ra
===> Có tất cả 16 dấu *
'''