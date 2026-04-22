# Project 1
def register_user(username, password):
  digits = 0
  alphabets = 0
  
  for i in password:
    if i.isdigit():
      digits += 1
    elif i.isalpha():
      alphabets += 1
  if len(password) >= 6 and digits >= 2 and alphabets >= 1:
    with open("accounts.txt", "a") as file:
      file.write(f"{username},{password}\n")
      print("Rigestered successfully")
      
  else:
    print("invalid password")
    
# login user
def login_user(username, password):
  found = False
  with open("accounts.txt", "r") as file:
    for line in file:
      stored_username, stored_password = line.strip().split(",")
      if stored_username == username and stored_password == password:
        print("login successfully")
        found = True
        break
  if not found:
    print("login failed")
    
register_user("nitishthakuur@gmail.com", "Bitcoin1405")

login_user("nitishthakuur@gmail.com", "Bitcoin1405")
    
    