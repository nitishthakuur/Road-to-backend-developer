# Q  1 print unique elements
s = input("enter the numbers")
n = set(s)
print(n)

# Q 2 remove duplicates form the list
s = [int(i) for i in input("enter the numbers").split()]
n = set(s)
print(n)


# Q 3 find common elements between two sets
a = set(int(i) for i in input("enter the numbers").split())
b = set(int(i) for i in input("enter the numbers").split())
print(a & b)

# Q 4 element present in first but not in second
a = set(int(i) for i in input("enter the numbers").split())
b = set(int(i) for i in input("enter the numbers").split())
print(a - b)

# Q 5 check if two lists have any common element
a = [int(i) for i in input("enter the numbers").split()]
c = set(a)
b = [int(i) for i in input("enter the numbers").split()]
d = set(b)
if c & d:
  print("yes, common elements exist")
else:
  print("no common elements")