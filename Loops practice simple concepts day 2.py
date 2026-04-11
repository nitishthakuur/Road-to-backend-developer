# While Loop

i = 1
while i <= 5:
	print(i)
	i += 1

# Q 1

i = 1
while i <= 10:
	print(i)
	i += 1
	
# Q2

i = 10
while i >= 1:
	print(i)
	i -= 1
	
# Q 3

n = 5
i = 1
while i <= n:
	print(i)
	i += 1	

# Q4

n = 5
i = 1

while i <= 5:
	if i % 2 ==0:
		print(i)
	i +=1
	
# Q 5

i = 1
while i <= 10:
	if i == 6:
		break
	print(i)
	i += 1
	
# Q 6

i = 1
while i <= 10:
	if i == 5:
		i +=1
		continue
		
	print(i)
	i += 1
	
# Q 7

i = 1
while i <= 10:
	if i % 7 ==0:
		break
		
	print(i)
	i += 1
	
# Nested Loops 
# Q 8

i = 1
for i in range(5):
	print("*")
	
# Q 9
for i in range(5):
		print("*", end= " ") 

# Q10

for i in range(1, 5):
	for j in range(i):
		print("*", end=" ")
	print()

# Q 11
for i in range(1, 5):
	for j in range(1, i+1):
		print(j, end= " ")
	print()
	
# Q 12

for i in range(1, 5):
	for j in range(1, i+1):
		print(chr(64+j), end= " ")
	print()

