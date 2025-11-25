def sum_normal(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def sum_recursive(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])
my_list = [10, 5, 2, 3]

print(f"Normal way: {sum_normal(my_list)}")
print(f"Recursive: {sum_recursive(my_list)}")