s = input("Enter a word or phrase: ")
count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)