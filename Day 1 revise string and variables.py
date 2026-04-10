s = "backend developer"

print(len(s))

# .count()

s = "Mississippi"
print(s.count("s"))
print(s.count("S"))

# case sensitivity
# ouput will be 1

# Remove spaces

s = "   python   "
print(s.strip())

# Replace

s = "banana"
print(s.replace("a", "*"))

# split

s = "one, two, three"
print(s.split(","))

# index + slicing
s = "user123@gmail.com"
index = s.index("@")

username = s[:index]
domain = s[index+1:]

print("username =", username)
print("domain =", domain)

# remove spaces
s = "hello world"
n =  ""
for i in s:
	if i != " ":
		n = n + i
		
print(n)

# reverse without slicing
s = "python"
v = ""
for i in s:
	v = i + v
	
print(v)


#s = s.strip() , here s is a new string without front and back spaces and s.strip() here s is a existing strip without front and back spaces 	