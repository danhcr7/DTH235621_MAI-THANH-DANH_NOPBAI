n = int(input("n: "))
def fib(n):
    i = 1 
    k = 1 
    l = 1
    while (i<=n):
        if (i==1 or i==2): print(k)
        elif(i==3): print(2)
        else:
            w = k+l
            l, w = w, l 
            k, w = w, k
            print(k+l)
        i += 1
fib(n)