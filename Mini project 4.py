def count(n):
  # count types
  alphabet = 0
  digits   = 0
  spaces   = 0
  special  = 0
  for i in n:
    if i.isalpha():
      alphabet +=1
    elif i.isdigit():
       digits += 1
    elif i == " ":
      spaces += 1
    else:
      special += 1
  return alphabet, digits, spaces, special
  
# reverse string
def rev(n):
  rev = ""
  for i in n:
    rev = i + rev
  return rev
  
# Clean string
def clean(n):
  n = n.replace(" ", "")
  n = n.lower()
  return n

n = input("enter what you want to")
alphabet, digits, spaces, special = count(n)
rev = rev(n)
n = clean(n)

print("alphabets =", alphabet)
print("digits =", digits)
print("spaces =", spaces)
print("special =", special)
print("reverse =", rev)
print("clean =", n)