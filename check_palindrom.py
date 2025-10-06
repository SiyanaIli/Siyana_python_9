words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]

palindromes = []

for word in words:
    if word == word[::-1]:  # потърсих за по лесен начин и намерих че [::-1] е думата наобратно и просто проверявам дали са верни
        palindromes.append(word)

print(palindromes)