with open("data.txt", "w") as file:
  file.write("Name = Nitish\nAge = 21")
  
with open("data.txt", "a") as file:
  file.write("\nlearning python")
  
with open("data.txt", "r") as file:
  print(file.read())
  
with open("data.txt", "w") as file:
  file.write("line1: Name = Nitish\nline 2: Age = 21\nline 3: Learning Python")
with open("data.txt", "r") as file:
  lines = file.readlines()
  
  for i in range(len(lines)):
    print(  lines[i].strip())
    
with open("users.txt","w") as file:
  file.write("Name = Nitish, Age = 21\nName = Rahul, Age = 20")
with open("users.txt", "r") as file:
  print(file.read())

with open("users.txt", "r") as file:
  lines = file.readlines()
  
  count = 0
  for i in lines:
    count +=1
  print(count)
  
# Add user (append)
def add_user(name, age):
    with open("users.txt", "a") as file:
        file.write(name + "," + age + "\n")


# View users
def view_users():
    with open("users.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")
            print("Name:", name, "Age:", age)


# Count users
def count_users():
    count = 0
    with open("users.txt", "r") as file:
        for line in file:
            count += 1
    return count


# --- TEST ---
add_user("Nitish", "21")
add_user("Rahul", "20")

print("Users:")
view_users()

print("Total users =", count_users())


    for line in file:
      name, age = line.strip().split(",")
      
      if name.lower() == search_name.lower():
        print("user found :", name, "Age :", age)
        found = True
        break
    if not found:
      print("user not found")
      # Add user (append)
def add_user(name, age):
  with open("users.txt", "a") as file:
    file.append(f"{name},{age}\n")
    
# View users
def view_users():
  with open("users.txt", "r") as file:
    for line in file:
      name, age = line.strip().split(",")
      print("Name", name, "Age", age)

# search users
def serch_users(search_name):
  found = False
  
  with open("users.txt", "r") as file:
# Delete users
def delete_user(delete_name):
  new_data = []
  found = False
  with open("users.txt", "r") as file:
    for line in file:
      name, age = line.strip().split()
      if name.lower() != delete_name.lower():
        new_data.append(line)
      else:
        found = True
        
  with open("users.txt", "w") as file:
    for line in file:
      file.write(line)
  
  if found:
    print("user deleted successfully")
  else:
    print("user not found")
      
# count users
def count_users():
  count = 0
  with open("users.txt", "r") as file:
    for line in file:
      count += 1
    return count
    
add_user = "Nitish", "21"
add_user = "ashish", "18"
add_user = "ritik", "23"
add_user = "simran", "21"
add_user = "akshay", "23"


print("total users :", count_users())

 for line in file:
      name, age = line.strip().split(",")
      
      if name.lower() == search_name.lower():
        print("user found :", name, "Age :", age)
        found = True
        break
    if not found:
      print("user not found")
      # Add user (append)
def add_user(name, age):
  with open("users.txt", "a") as file:
    file.append(f"{name},{age}\n")
    
# View users
def view_users():
  with open("users.txt", "r") as file:
    for line in file:
      name, age = line.strip().split(",")
      print("Name", name, "Age", age)

# search users
def serch_users(search_name):
  found = False
  
  with open("users.txt", "r") as file:
# Delete users
def delete_user(delete_name):
  new_data = []
  found = False
  with open("users.txt", "r") as file:
    for line in file:
      name, age = line.strip().split()
      if name.lower() != delete_name.lower():
        new_data.append(line)
      else:
        found = True
        
  with open("users.txt", "w") as file:
    for line in file:
      file.write(line)
  
  if found:
    print("user deleted successfully")
  else:
    print("user not found")
      
# count users
def count_users():
  count = 0
  with open("users.txt", "r") as file:
    for line in file:
      count += 1
    return count
    
add_user = "Nitish", "21"
add_user = "ashish", "18"
add_user = "ritik", "23"
add_user = "simran", "21"
add_user = "akshay", "23"

print("users :", view_users())
print("total users :", count_users())
  