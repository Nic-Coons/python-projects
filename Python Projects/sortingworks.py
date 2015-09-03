ls = [67, 45, 2, 13, 1, 998]
print (ls)

def inPlace(x):
    x.sort()
inPlace(ls)

print (ls)

ls.reverse()

print (ls)

def bubblesort(ls):
    for numb in range(len(ls)-1,0,-1):
        for i in range(numb):
            if ls[i]>ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp

bubblesort(ls)

print (ls)
