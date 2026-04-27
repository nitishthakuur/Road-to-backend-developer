
# Print 1 to n:
def print_n(n):
  if n == 0:
    return
 
  print_n(n - 1)
  print(n)
  
n = int(input("enter the n"))
print_n(n)

# Print n to 1:
def print_n(n):
  if n == 0:
    return
  print(n)
  print_n(n-1)
  
n = int(input("enter the n"))
print_n(n)

# sum of n:
def sum_n(n):
  if n == 0:
    return 0
  return n + sum_n(n - 1)
  sum_n(n)
  
n = int(input("enter the value of n"))
print(sum_n(n))

def fact(n):
  if n == 0:
    return 1
  return n * fact(n-1)
  
n = int(input("enter the n: "))
print(fact(n))

# Q5 power(a^b)
def power(a, b):
  if b == 0:
    return 1
  return a* power(a,b-1)
  
a = int(input("enter the a :"))
b = int(input("enter the b:"))
print(power(a, b))

# Intermediate level practice:
# Sum of digits:
def sum_d(n):
  if n == 0:
    return 0
  return (n % 10) + sum_d(n // 10)
  
n = int(input("enter the number"))
print(sum_d(n))

# Count of digits
def count_d(n):
  if n == 0:
    return 0
  return 1 + count_d(n // 10)
n = int(input("enter the n: "))
if n == 0:
  print(1)
else:
  print(count_d(n))
  
# Reverse a number
def rev_num(n, rev):
  if n == 0:
    return rev
  rev = rev * 10 + (n % 10)
  return  rev_num(n // 10, rev)
  
n = int(input("enter the n: "))
print(rev_num(n, 0))

# Palindrome number
def palin(n, rev):
  if n == 0:
    return rev
  rev = rev * 10 + (n % 10)
  return palin(n // 10, rev)
n = int(input("enter the n :"))
original = n
reversed_num = palin(n, 0)

if original == reversed_num:
  print("palindrome")
else:
  print("Not palindrome")
  
# Reverse a string:
def rev_str(n):
  if n == "":
    return ""
  
  return rev_str(n[1:]) + n[0]
  
n = input("enter the string")
print(rev_str(n))

# Final Task
def palin_str(n):
  if len(n) <= 1:
    return True
  
  if n[0] != n[-1]:
    return False
  
  return palin_str(n[1:-1])
n = input("enter the string")
if palin_str(n):
  print("Plaindrome")
else:
  print("not Palindrome")
