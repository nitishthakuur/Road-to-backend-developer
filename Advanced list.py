# Q 1
nums = [1, 2, 3, 4, 5]
print(nums[:3])
print(nums[3:])

# Q 2
nums = [10, 20, 30, 40]
print(nums[::-1])

# list comprehension
#["expression for item" "in list" "if condition""]
# Advanced level
 # Q 3
nums = [1, 2, 3, 4, 5]
squares = [i*i for i in nums]
print(squares)

# Q 4
nums = [1, 2, 3, 4, 5, 6]
even_num = [i for i in nums if i % 2 == 0]
print(even_num)

#Sorting means it arrange the list
# list.sort() accending
# list.sort(reverse=True) decending

# Q 5
nums = [3, 1, 4, 2]
nums.sort()
print(nums)

# Q 6 reverse sorting
nums = [3, 1, 4, 2]
nums.sort(reverse=True)
print(nums)

# Mini Project
nums = [10, 5, 20, 15, 30, 25]

even_num= [i for i in nums if i % 2 == 0]
print("even =", even_num)

squares = [i*i for i in nums]
print("squares =", squares)

nums.sort()
print("accending =", nums)

nums.sort(reverse=True)
print("decending =", nums)

print("reversed", nums[::-1])