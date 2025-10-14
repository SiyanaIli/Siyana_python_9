while True:
    print("\n=== Calculator ===")
    a = float(input("Number one: "))
    b = float(input("Number two: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("enter: ").strip().lower()

    if choice in ("1", "add"):
        print(f"Result: {a} + {b} = {a + b}")
    elif choice in ("2", "subtract"):
        print(f"Result: {a} - {b} = {a - b}")
    elif choice in ("3", "multiply"):
        print(f"Result: {a} * {b} = {a * b}")
    elif choice in ("4", "divide"):
        if b == 0:
            print("Error")
        else:
            print(f"Result: {a} / {b} = {a / b}")
    elif choice in ("5", "exit"):
        print("Bye bye lil bitches")
        break
    
