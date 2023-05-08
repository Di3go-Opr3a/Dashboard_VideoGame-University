list = [1,2,1,3,2,5,3]

for x in list: 
    posizione = list.index(x)
    print(posizione, x)

print(" ")

for x in range(len(list)):
    print(x, list[x])