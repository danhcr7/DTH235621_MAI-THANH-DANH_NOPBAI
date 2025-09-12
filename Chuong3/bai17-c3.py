"""
done = False
n, m = 0, 100
while not done and n!=m:
    n = int(input())
    if (n<0):
        done = True
    print("n =", n)
"""
'''Nhập n cho tới khi nó < 0 hoặc =m thì dừng lại'''
m = 100
while (True):
    n = int(input())
    if (n<0 or n==m): break
