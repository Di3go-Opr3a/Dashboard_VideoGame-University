list = [0,1,2,3,4,5]
count = len(list) - 1 

for x in range(len(list)):
    print(x)
    if x == count:
        break
    list.pop(1)
    print(x)