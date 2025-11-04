numbers = input("Please enter numbers separated by comma: ")  # Взимаме от input числата разделени с запетая
numbers = numbers.split(",")  # Разделяме стринга на списък по запетая
max_odd = 0
for i in numbers:
    if int(i) % 2 == 1:  # Ако е нечетно проверяваме дали е по-голямо от текущото най-голямо
        if max_odd <= int(i):
            max_odd = i
if max_odd:
    print(max_odd)
else:
    print("There are no odd numbers")