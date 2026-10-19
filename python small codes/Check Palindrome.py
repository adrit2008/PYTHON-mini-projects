a = "code"
reverse = ""

for y in a:
    reverse = y + reverse

if a == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")