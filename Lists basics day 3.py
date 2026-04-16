nums = [10, 20, 30, 40]
print(nums[0])
print(nums[-1])

# Q 2

nums = [5, 10, 15, 20]
for i in nums:
	print(i)
	
# Q3
nums = [1, 2, 3, 4, 5]
sum = 0
for i in nums:
	sum +=i
	
print(sum)	

# Append.()
# Q4
nums = [1, 2, 3]
nums.append(4)
print(nums)

# insert means insert at specific place
# Q 5
nums = [10, 20, 30]
nums.insert(1, 15)
print(nums)

#Remove 
# Q 6
nums = [5, 10, 15, 10]
nums.remove(10)
print(nums)

# Pop
# Q 7
nums = [100, 200, 300]
nums.pop(1)
print(nums)

# Practice 
# Q 8
nums = [10, 20, 30, 40]
max_val = nums[0]
for i in nums:
	if i > max_val:
		max_val = i

print(max_val)

# Q 9
nums = [5, 2, 9, 1]
min_val = nums[0]
for i in nums:
	if i < min_val:
		min_val = i
		
print(min_val)

#Q 10
nums = [1, 2, 3, 2, 4, 2]
count_2 = 0
for i in nums:
	if i == 2:
		count_2 += 1
		
print(count_2)

# Q 11
nums = [1, 2, 3, 4, 5]
even_nums = []
for i in nums:
	if i % 2 == 0:
		even_nums.append(i)
		
print(even_nums)

# mini project
nums = [10, 5, 20, 5, 30]
max_val= nums[0]
min_val= nums[0]
count_5 =0
even_nums = []
for i in nums:
	if i > max_val:
		max_val = i
	if i < min_val:
		min_val = i
	if i == 5:
		count_5 += 1
		
	if i % 2 == 0:
		even_nums.append(i)
			
print(max_val)
print(min_val)
print(count_5)
print(even_nums)
