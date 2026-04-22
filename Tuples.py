# Q 1 sum of tuple
t = tuple(int(i) for i in input("enter the tuple").split())
total = 0
for i in t:
  total += i
print(total)

# |Q 2 max value
t = tuple(int(i) for i in input("enter the tuple").split())
max_value = t[0]
for i in t:
  if i > max_value:
    max_value = i
print(max_value)

# Q 3 swap using tuples
a, b = (10, 20)
print("a = ",a, "b =",b)
a,b = b,a
# print after swap
print("a =", a, "b =", b)

# Q 4 function return
def tuples(num):
  total = 0
  maximum = num[0]
  for i in num:
    total +=i
    if i > maximum:
      maximum = i
  return total, maximum
  
num = tuple(int(i) for i in input("enter the tuple").split())
total, maximum = tuples(num)
print("total =", total)
print("maximum =", maximum)
# Q 5 find count
t = (1, 2, 2, 3, 2)
print(t.count(2))
