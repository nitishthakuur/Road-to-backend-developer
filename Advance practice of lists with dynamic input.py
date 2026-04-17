# Q 1 practice of lists in dynamic input

nums = [int(i)  for i in input(). split()]

total = 0
for i in nums:
	total += i
	
print(total)

# Q2
nums = [int(i) for i in input(). split()]
max_num = nums[0]
for i in nums:
	if i > max_num:
		max_num = i
		
print(max_num)

# Q 3

nums = [int(i) for i in input().split()]
even_num = []
for i in nums:
	if i % 2 ==0:
		even_num.append(i)
		
print(even_num)

# Q 4
nums= [int(i) for i in input().split()]
rev_num = []
for i in nums:
	rev_num = [i] + rev_num
	
print(rev_num)

#Q 5 Remove duplicates
nums = [int(i) for i in input() .split()]
rem_duplicate =  []
for i in nums:
	if i not in rem_duplicate:
		rem_duplicate.append(i)
		
print(rem_duplicate)	