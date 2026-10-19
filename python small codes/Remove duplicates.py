n = [1, 2, 2, 3, 4, 4, 5]
unique_n = []

for num in n:
    found = False

    for i in unique_n:
        if i == num:
            found = True
            break
    if not found:
        unique_n.append(num)

print(unique_n)