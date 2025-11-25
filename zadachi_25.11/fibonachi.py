def fib_normal(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

n_number = 8 

print(f"Normal way (F{n_number}): {fib_normal(n_number)}")
print(f"Recuesive (F{n_number}): {fib_recursive(n_number)}")