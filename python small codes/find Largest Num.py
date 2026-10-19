nums = [5, 3, 8, 2, 10]
largest_num = nums[0]

for n in nums:
    if n > largest_num:
        largest_num = n

print(largest_num)