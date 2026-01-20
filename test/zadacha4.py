def is_power_of_three(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1
inter_input = int(input("Enter an number: "))
result = is_power_of_three(inter_input)
if result:
    print(f"{inter_input} is a power of three.")
else:
    print(f"{inter_input} is not a power of three.")


