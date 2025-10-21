import random
n = random.randint(1, 10) 
print(f"there will be {n} files ")

for i in range(1, n + 1):
    filename = f"random_file_{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{i}.\n")
    print(f"We created a file: {filename}")
