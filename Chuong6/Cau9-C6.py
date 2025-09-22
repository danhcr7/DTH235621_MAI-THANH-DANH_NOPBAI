n = int(input())
l = []
def snt(n):
    if (n<2): return False 
    # n>=2
    check = 0
    for i in range(1, n+1):
        if (n%i == 0): check += 1 
    if (check != 2): return False
    return True
for i in range(n):
    x = int(input())
    l.append(x)
# gồm các số lẻ,chẵn tổng cộng có bao nhiêu số lẻ, chẵn:
tongsole, tongsochan = 0, 0
for i in l:
    if (i%2 != 0):
        print(i, end = ' ')
        tongsole += 1 
    if (i%2 == 0):
        tongsochan += 1 
print(tongsole)
for i in l:
    if (i%2 == 0): 
        print(i, end = ' ')
print(tongsochan)
# snt:
for i in l:
    if (snt(i)): 
        print(i, end = ' ')
        # snt:
# không là snt:
print()
for i in l:
    if (snt(i) == False): 
        print(i, end = ' ')