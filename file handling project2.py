# add contacts
def add_contacts(name, phone):
  with open("contacts.txt", "a") as file:
    file.write(f"{name},{phone}\n")

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
      
      if search_name == name:
        print("user found :", name, "Phone :", phone)
        found = True
        break
  if not found:
    print("user not found")
    
#Delete contacts
def delete_contacts(delete_name):
  new_list = []
  found = False
  with open("contacts.txt", "r") as file:
    for line in file:
      name, phone = line.strip().split(",")
      if delete_name != name:
        new_list.append(line)
      else:
        found = True
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
  
add_contacts ("Nitish", "6230077616")
add_contacts ("Ashish", "7018075043")
add_contacts ("Prakash", "9418717212")
add_contacts ("seema", "9459568912")

print("contacts:\n")
view_contacts()

print("search contact")
search_contacts("Ashish")

print("deleted contacts")
delete_contacts("Prakash")

print("count:", count_contacts())

print("after delete")
view_contacts()
