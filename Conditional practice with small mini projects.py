# Q1

x = 15
if x > 10:
	print("greater than 10")
	
else:
		print("10 or less than 10")
		
# Q2

x = 7
if x % 2 == 0:
	print("even")
	
else:
		print("odd")	
		
# Q3

x = 0

if x > 0:
	print("positive")
	
elif x < 0:
	print("negative")
	
else:
		print("zero")
		
# Q4

x = 25

if x % 5 == 0:
	print("divisible by 5")
	
else:
		print("not divisible")
		
# Q5

x = 15

if x > 10 and x < 20:
	print("between 10 and 20")
	
else:
		print("not in between")
		
# Q6

x = 3

if x<5 or x>20:
	print("out of range")
	
else:
		print("between 5 and 20")
		
# Q7

x = 10

if not x > 10:
	print("not greater than 10")
	
else:
		print("greater than 10")
		
		
# Q 8

x = 25
if x > 10:
	if x % 2 == 0:
		print("even and greater than 10")
	else:
			print("odd and greater than 10")
			
else:
		print("less than 10")			
# Q 9

x = -5
if x > 0:
		if x %2 == 0:
			print("positive and even")
		else:
				print("positive and odd")
				
else:
		print("not positive")
		
# Q 10 password validation 

password = "abc123"

length = len(password)

has_digit = False

for i in password:
	if i.isdigit():
		has_digit =True
if length >= 6 and has_digit:
		print("valid password")
else:
			print("invalid password")
			
# Q 11 password program

password = input("enter the password")

length = len(password)
digit_count = 0
alphabet_count= 0

for i in password:
	if i.isdigit():
		digit_count +=1
		
	if i.isalpha():
		alphabet_count += 1
		
if length >= 6 and digit_count > 1 and alphabet_count > 0:
	print("valid password")
	
else:
		print("invalid password")		