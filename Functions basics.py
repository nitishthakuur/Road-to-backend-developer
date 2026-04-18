 greet(name):
    print("hello", name)

greet("Nitish")

#Q 2 printing squares
def square(numbers):
  return numbers*numbers
  
numbers = int(input("enter the number"))
print(square (numbers))

# Q 3 even and odd 
def even_odd(number):
  if number % 2 == 0:
    result = "even"
  
  else:
    result = "odd"
  return result
number = int(input("enter the number"))
print(even_odd(number))

# Q 4
def total_all(numbers):
  total = 0
  for i in numbers:
    total += i
  return total
numbers = [int(i) for i in input().split()]
print(total_all(numbers))

# Q 5 Max numbers
def maximum(numbers):
  max_num = numbers[0]
  for i in numbers:
    if i> max_num:
      max_num = i
  return max_num
  
numbers = [int(i) for i in input().split()]
print(maximum(numbers))

# function returning multiple values
def multiple(list_):
  total = 0
  max_num = list_[0]
  for i in list_:
    total += i
    if i > max_num:
      max_num = i
  return total, max_num
  
list_ = [int(i) for i in input().split()]
total, max_num = multiple(list_)
print("sum =", total)
print("max =", max_num)

# function + problem solving
def even_odd(numbers):
  even_list = [i for i in numbers if i % 2 == 0]
  odd_list  = [i for i in numbers if i % 2 != 0]
  return even_list, odd_list
numbers = [int(i) for i in input().split()]
even_list, odd_list = even_odd(numbers)
print("even list =", even_list)
print("odd list =", odd_list)

# now funciton with string
def alphabet(string):
  count_vowel     = 0
  count_consonant = 0
  vowel           = "aeiou"
  string = string.lower()
  for i in string:
    if i.isalpha():
      if i in vowel:
        count_vowel += 1
      else:
        count_consonant += 1
  return count_vowel, count_consonant
string = input("enter the string")
count_vowel, count_consonant = alphabet(string)
print("vowel =", count_vowel)
print("consonant =", count_consonant)

# Final Bow before moving to the advance level
def final(string):
  rev_string = ""
  string = string.lower()
  for i in string:
    rev_string = i + rev_string
    
  if rev_string == string:
    palindrome = True
     
  else:
    palindrome = False
  return rev_string, palindrome
string = input("enter the string")
rev_string, palindrome = final(string)
print("reverse =", rev_string)
print("palindrome", palindrome)
    
