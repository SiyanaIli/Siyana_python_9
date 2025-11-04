numbers = [4, 5, 6, 6, 7, 9, 1, 1]
output = []  # Изходен списък, в който ще слагаме уникалните числа
for i in numbers:
    if i in output:  # Проверка дали вече го има числото в изходния списък
        continue
    output.append(i)
output.reverse()  # Функцията прави in-place обръщане на списъка, т.е. не се налага да го присвояваме на променлива
print(output)