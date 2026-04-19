def user(email, password):
  # valid email
  valid_email = False
  if email.count("@") == 1 and " " not in email:
    index = email.index("@")
    if index != 0 and index != len(email) -1:
      if "." in email[index:]:
        valid_email = True
  #valid password
  length = len(password)
  digits = 0
  alphabet = 0
  for i in password:
    if i.isdigit():
      digits += 1
    if i.isalpha():
      alphabet += 1
        
  valid_password = False
  if length >= 6 and digits >= 2 and alphabet >= 1:
    valid_password = True
  if valid_email and valid_password:
    return "valid user"
  else:
    return "invalid user"
email = input("enter the email")
password = input("enter the password")
print(user(email, password))