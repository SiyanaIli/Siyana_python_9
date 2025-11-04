txt = input("Enter the text: ")
lets = {} 
for i in txt:  
    if i in ".,!?;:()-' \n":  
        continue
    let = i.lower() 
    if let in lets:
        lets[let] += 1
    else:
        lets[let] = 1
max = max(lets.values()) 
for key in lets:  
    if lets[key] == max:
        max_key = key
print(lets)
print (f"The most frequent letter is '{max_key}' which appears {max} times.")