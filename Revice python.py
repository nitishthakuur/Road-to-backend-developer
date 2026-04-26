'''# Student Record system
open("students.txt", "a").close()

def add_student(name, marks):
  with open("students.txt", "a") as file:
    file.write(f"{name},{marks}\n")
    print("student added")
    
def view_students():
  with open("students.txt", "r") as file:
    for line in file:
      name, marks = line.strip().split(",")
      print("Name :", name, "Marks :", marks)
      
def search_student(search_name):
  found = False
  with open("students.txt", "r") as file:
    for line in file:
      name, marks = line.strip().split(",")
      if name.lower() == search_name.lower():
        print("Name :", name, "Marks :", marks)
        found = True
        break
  
  if not found:
    print("student not found")
    
def delete_student(delete_name):
  found = False
  new_list = []
  with open("students.txt", "r") as file:
    for line in file:
      
      name, marks = line.strip().split(",")
      if name.lower() != delete_name.lower():
        new_list.append(line)
      else:
        found = True
      
  with open("students.txt", "w") as file:
    for line in new_list:
      file.write(line)
  
  if found:
    print("Deleted the student succesfully")
  else:
    print("student not found")
    
def topper():
  with open("students.txt", "r") as file:
    first_line = file.readline().strip()
    
    if not first_line:
      print("No student found")
      return
     
    name,marks = first_line.strip().split(",")
    max_marks = int(marks)
    topper = name
    for line in file:
       name, marks = line.strip().split(",")
       if int(marks) > max_marks:
         max_marks = int(marks)
         topper = name
    return topper, max_marks
 
        
def average_marks():
  total = 0
  count = 0
  with open("students.txt", "r") as file:
    for line in file:
      name, marks= line.strip().split(",")
      total += int(marks)
      count += 1
  if count == 0:
    print("No students found")
    return 0
    
  average = total / count
  return average
  
  
# Menu system
while True:
  print("choose operations\n")
  print("1. add Students")
  print("2. view Students")
  print("3. search Students")
  print("4. Delete Students")
  print("5. topper")
  print("6. average marks")
  print("7. exit")

  choice = input("enter your choice")
  
  if choice == "1":
    name = input("enter the name")
    marks = input("enter the marks")
    add_student(name, marks)
    
  elif choice == "2":
    view_students()
  
  elif choice == "3":
    search_name = input("enter the name you want to search")
    search_student(search_name)
  
  elif choice == "4":
    delete_name = input("enter the name you want to delete")
    delete_student(delete_name)
    
  elif choice == "5":
    topper, max_marks = topper()
    print("Topper :", topper, "Marks :", max_marks)
    
  elif choice == "6":
    average = average_marks()
    print("Average :", average)
    
  elif choice =="7":
    print("exiting")
    break
  else:
    print("invalid input")
    
# Mini project 2
# Number Analyzer
num = []
def add_num():
  global num
  num = [int(i) for i in input("enter the numbers:").split()]
  print("Numbers added")
# Show all numbers
def view_num():
  if not num:
    print("No numbers available")
    return
  print("Numbers :",num)

# find sum
def sum_num():
  if not num:
    print("No number available")
    return
  
  total = 0
  for i in num:
    total += i

  print("total :", total)

# find maximum
def max_number():
  if not num:
    print("NO number available")
    return
  
  max_num = num[0]
  for i in num:
    if i > max_num:
      max_num = i

  print("maximum number :", max_num)

# Even numbers
def even_num():
  if not num:
    print("NO number available")
    return
  
  even_num = [i for i in num if i % 2 == 0]
  print("Even numbers :", even_num)

# Remove duplicates
def remove_duplicates():
  if not num:
    print("No number available")
    return
  print("Duplicates Removed :", list(set(num)))
  
# Menu system
while True:
  print("\nchoose operation")
  print("1. add number")
  print("2. view number")
  print("3. sum of number")
  print("4. maximum")
  print("5. even number")
  print("6. after duplicates")
  print("7. exit")
  choice = input("enter the choice")
  if choice == "1":
    add_num()
  
  elif choice == "2":
    view_num()
    
  elif choice == "3":
    sum_num()
    
  elif choice == "4":
    max_number()
    
  elif choice == "5":
    even_num()
    
  elif choice == "6":
    remove_duplicates()
    
  elif choice == "7":
    print("exiting")
    break
  else:
    print("invalid choice")
    
# Mini project 3
# Password validator
password = input("enter the password")
digits = 0
alphabets = 0
upper_case = 0
lower_case = 0
special_char = 0
length = len(password)
for i in password:
  if i.isdigit():
    digits += 1
  elif i.isalpha():
    alphabets += 1
    if i.isupper():
      upper_case += 1
    elif i.islower():
      lower_case += 1
  elif i != " ":
    special_char += 1
  
if length >= 6 and digits >= 1 and alphabets >= 1 and upper_case >= 1 and lower_case >= 1 and special_char >= 1:
  print("strong password")
else:
  print("weak password")'''
  
# Mini project 4
# Bank system

# Create account:
def create_ac():
  account_created = False
  name = input('enter the name')
  initial_bal = int(input("enter the initial balance"))
  if initial_bal >= 0:
    print("Account created succesfully")
    account_created = True
  else:
    print("(Invalid balance. Account not created)")
    account_created = False
  return account_created, name, initial_bal
  
# Deposite funcitonL:
def deposite_amt(balance, account_created):
  
  if not account_created:
    print("account not created")
    return balance
  amount = int(input("enter the deposite amount"))
  if amount > 0:
    balance = balance + amount
    print("Amount added successfully")
  else:
    print("invalid input")
  return balance
  
# Widraw function:
def widraw_amt(balance, account_created):
  
  if not account_created:
    print("account not created")
    return balance
  amount = int(input("enter the widrawn amount"))
  
  if amount <= 0:
    print("invalid input")
    return balance
    
  elif amount > balance:
    print("insufficient funds")
    return balance
    
  else:
    print("Amount widrawn successfully")
    balance = balance - amount
  
  return balance
  
# Menu system
balance = 0
account_created = False
name = ""
while True:
  print("choose operation")
  print("1. create Account")
  print("2. Add Amount")
  print("3. Withdrawn Amount")
  print("4. exit")
  
  choice = input("enter the choice")
  
  if choice == "1":
    account_created,name,balance = create_ac()
    
  elif choice == "2":
    balance = deposite_amt(balance, account_created)
    
  elif choice == "3":
    balance = widraw_amt(balance, account_created)
    
  elif choice == "4":
    print("exiting")
    break
  else:
    print("invalid input")
  

    
    
    



    
  