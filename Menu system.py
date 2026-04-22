open("contacts.txt", "a").close()
  
# add contacts
def add_contacts(name, phone):
  with open("contacts.txt", "r") as file:
    for line in file:
      existing_name, _ = line.strip().split(",")
      
      if existing_name.lower() == name.lower():
        print("contact already exists")
        return
      
  with open("contacts.txt", "a") as file:
    file.write(f"{name},{phone}\n")
    
  print("contact added")

      
# view contacts
def view_contacts():
  with open("contacts.txt", "r") as file:
    for line in file:
      name, phone = line.strip().split(",")
      print("Name", name, "phone", phone)


#search contacts:
def search_contacts(search_name):
  found = False
  with open("contacts.txt", "r") as file:
    for line in file:
      name, phone = line.strip().split(",")
      
      if search_name.lower() == name.lower():
        print("user found :", name, "Phone :", phone)
        found = True
        break
  if not found:
    print("user not found")
    
#Delete contacts
def delete_contacts(delete_name):
  choice = input("Are you sure you want to delete? (yes/no): ")
  if choice.lower() != "yes":
    print("delete cancelled")
    return
  new_list = []
  found = False
  with open("contacts.txt", "r") as file:
    for line in file:
      name, phone = line.strip().split(",")
      if delete_name.lower() != name.lower():
        new_list.append(line)
      else:
        found = True
  # add list to the file      
  with open("contacts.txt", "w") as file:
    for line in new_list:
      file.write(line)
      
  if found:
    print("deleted successfully")
  else:
    print("user not found")
    
# count contacts
def count_contacts():
  count = 0
  with open("contacts.txt", "r") as file:
    for line in file:
      count += 1
  return count
  
# Menu system
while True:
  print("\nchoice operation")
  print("1. add_contacts")
  print("2. view_contacts")
  print("3. search_contacts")
  print("4. delete_contacts")
  print("5.count_contacts")
  print("6. exit")

  choice = input("enter the choice")
  if choice == "1":
    name = input("enter the name")
    phone = input("enter the phone")
    add_contacts(name, phone)
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    search_name = input("enter the name")
    search_contacts(search_name)
  elif choice == "4":
    delete_name = input("enter the name")
    delete_contacts(delete_name)
  elif choice == "5":
    print("count = ", count_contacts())
  elif choice == "6":
    print("exiting ")
    break
  else:
    print("invalid input")