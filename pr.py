a=[]
for i in range(5):
    i = int(input("enter number: "))
    a.append(i)
    if (i%2==1):
        print("odd")
    else: print("even")
print (a)
