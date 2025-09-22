lst = [3, 0, 1, 5, 2]
x = 2
# lst[0]: In ra phần tử đầu tiên của list ---> ra 3 
print(lst[0])
# lst[3]: In ra phần tử có Index = 3 ---> ra 5 
print(lst[3])
# lst[x]: vì x = 2 nên lst[x] = lst[2] ---> ra 1 
print(lst[x])
# lst[-x]: vì x = 2 --> -x = -2 ---> lst[-x] = lst[-2] ---> ra 5
print(lst[-x])
# lst[x+1]: vì x = 2 nên x+1 = 3 ---> lst[x+1] = lst[3] ---> ra 5 
print(lst[x+1])
# lst[x] + 1: lst[x] = lst[2] = 1 ---> lst[x] + 1 = 1 + 1 = 2  
print(lst[x] + 1)
# lst[lst[x]]: lst[x] = lst[2] = 1 ---> lst[lst[x]] = lst[1] = 0
print(lst[lst[x]])
# lst[lst[lst[x]]]: lst[lst[1]] = lst[0] = 3 
print(lst[lst[lst[x]]])
