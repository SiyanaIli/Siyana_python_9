numbers = [1,2,4,4,7,9,9,3,3]
output = []
for i in numbers:
    if i in output: 
        continue
    output.append(i)
print("List with duplicates:")
print(numbers)
print("List without duplicates:")
print(output)