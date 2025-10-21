n = int(input("Enter: "))

for i in range(1, n + 1):
    filename = f"file_{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"File number{i}.\n")
    print(f"We created a file: {filename}")
