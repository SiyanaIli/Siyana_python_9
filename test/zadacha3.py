def dividers(n):
    divs = []
    for i in range(2, n):
        if n % i == 0:
            divs.append(i)   
    return divs
input_number = int(input("Enter a number: "))
result = dividers(input_number)
if result:
    print(f"{input_number} has the following dividers: {result}")
else:
    print(f"{input_number} has no dividers.")