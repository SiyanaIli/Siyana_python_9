numbers=[5,12,18,21,33,42,50,77,90]

special_numbers=[]
for m in numbers:
    if (m>20 and m%3==0 and m%5!=0):
        special_numbers.append(m)

print(special_numbers)