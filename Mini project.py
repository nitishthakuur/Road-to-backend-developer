def cart(numbers):
  # Total price
  total = 0
  for i in numbers:
    total += i
    
  # Unique Items
  unique = []
  for i in numbers:
    if i not in unique:
      unique.append(i)
  #frequency    
  d = {}
  for i in numbers:
    if i in d:
      d[i] += 1
    else:
      d[i] =1

  
  return total, unique,d
  
numbers = [10, 20, 30, 20, 40, 10]
total, unique, d = cart(numbers)
print("total =", total)
print("unique =", unique)
print("frequency =", d)
  