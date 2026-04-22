# Add user
def add_user(name, age):
    with open("users.txt", "a") as file:
        file.write(f"{name},{age}\n")


# View users
def view_users():
    with open("users.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")
            print("Name:", name, "Age:", age)


# Search user
def search_user(search_name):
    found = False
    with open("users.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")
            if name.lower() == search_name.lower():
                print("User found:", name, "Age:", age)
                found = True
                break

    if not found:
        print("User not found")


# Delete user
def delete_user(delete_name):
    new_data = []
    found = False

    with open("users.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")
            if name.lower() != delete_name.lower():
                new_data.append(line)
            else:
                found = True

    with open("users.txt", "w") as file:
        for line in new_data:
            file.write(line)

    if found:
        print("User deleted successfully")
    else:
        print("User not found")


# Count users
def count_users():
    count = 0
    with open("users.txt", "r") as file:
        for line in file:
            count += 1
    return count


# --- TEST ---
add_user("Nitish", "21")
add_user("Ashish", "18")
add_user("Ritik", "23")

print("\nUsers:")
view_users()

print("\nTotal users:", count_users())

'''print("\nSearch:")'''
search_user("Nitish")

print("\nDelete:")
delete_user("Ashish")

print("\nAfter deletion:")
view_users()