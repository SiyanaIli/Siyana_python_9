def rev_normal(s):
    return s[::-1]

def rev_recursive(s):
    if len(s) <= 1:
        return s
    else:
        return rev_recursive(s[1:]) + s[0]
my_string = "Programing"

print(f"Normal way: {rev_normal(my_string)}")
print(f"Recursive: {rev_recursive(my_string)}")