n = int(input("Enter a number: "))
prime = True
if n < 2:
    prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1

    print("Prime" if prime else "Not Prime")