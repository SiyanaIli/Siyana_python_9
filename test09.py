s = input("Enter a sentence: ")
letters = {}  # Тук ще държим символите и тяхната срещаност - ключа е буквата, стойността е броя срещания
for i in s:  # Обхождаме всеки символ
    if i in "!,?. ":  # Проверка дали не е препинателен знак
        continue
    letter = i.lower()  # Правим буквата малка
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1
max_value = max(letters.values())  # Намираме най-голямата бройка с функцията max
for key in letters:  # Обхождаме речника и търсим ключа, където стойността съвпада
    if letters[key] == max_value:
        max_key = key
print(max_key, max_value)