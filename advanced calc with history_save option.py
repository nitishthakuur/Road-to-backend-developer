open("history.txt", "a").close()

def add(a, b):
	return a + b
	
def sub(a, b):
	return a - b
	
def multi(a, b):
	return a * b
	
def dvd(a, b):
	if b == 0:
		print("cannot divide by 0")
	else:
		return a / b
		
def save_history(text):
	with open("history.txt", "a") as file:
		file.write(text + "\n")
		
def view_hist():
	with open("history.txt", "r") as file:
		data = file.read()
		
		if data == "":
			print("No History found")
			
		else:
			print("History :")
			print(data)
	
while True:

	print("Choose operations")
	print("1. addition")
	print("2. subtraction")
	print("3. multiplication")
	print("4. division")
	print("5 view history")
	print("6 exit")
	choice = input("enter the choice")
	
	if choice == "6":
		print("exiting")
		break
		
	if choice == "5":
		view_hist()
		continue
	try:
		a = int(input("enter the number 1"))
		b = int(input("enter the number 2"))
		
		if choice == "1":
			result = add(a, b)
			operation = f"{a} + {b} = {result}"
		
		elif choice == "2":
			result = sub(a, b)
			operation = f"{a} - {b} = {result}"
		
		elif choice == "3":
			result = multi(a, b)
			operation = f"{a} * {b} = {result}"
		
		elif choice == "4":
			result = dvd(a, b)
			operation = f"{a} / {b} = {result}"
		
		else:
			print("invalid input")
			continue
			
		print("Result :", result)
		
		save_history(operation)
		
	except ValueError:
		print("please enter the valid integer")
		
	except ZeroDivisionError:
		print("cannot divide by zero")