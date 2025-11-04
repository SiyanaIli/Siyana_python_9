numbers = input("Please enter numbers: ") 
numbers = numbers.split(" ") 
max_of_odd = 0
for i in numbers:
    if int(i) % 2 == 1:
        if max_of_odd <= int(i):
            max_of_odd = i
if max_of_odd:
    print(max_of_odd)
else:
    print("There are no odd numbers, only even ones.")