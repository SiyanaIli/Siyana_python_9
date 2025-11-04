original_list = ["cat", "dog", "elephant", "sun", "moon", "hi"]
short_strings = []
for string in original_list:
    if len(string) < 4:
        short_strings.append(string)
print("Стрингове с по-малко от 4 символа:", short_strings)