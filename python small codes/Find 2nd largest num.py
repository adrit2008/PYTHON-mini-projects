nums = [5, 10, 3, 8, 15]
largest = nums[0]
second_largest = 0

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("Second largest number is:", second_largest)