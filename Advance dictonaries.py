s = "banana"
d = {}
for char in s:
	if char in d:
		d[char] += 1
	else:
		d[char] = 1
		
for key in d:
	print(key, ":",  d[key])
	
# Q2
s = "mississippi"
d = {}
for char in s:
	if char in d:
		d[char] += 1
	else:
		d[char] = 1
for key in d:
	print(key, ":", d[key])
	
#Q 3
s = "banana"
d = {}
for char in s:
	if char in d:
		d[char] += 1
	else:
		d[char] = 1
max_count = 0
max_char = ""
for key in d:
	if d[key] > max_count:
		max_count = d[key]
		max_char = key
print(max_char, ":", max_count)

# Q 4
s = "aabbcc"
d = {}
for char in s:
	if char in d:
		d[char] += 1
	else:
		d[char] = 1
max_count = 0
for key in d:
	if d[key]>max_count:
		max_count = d[key]
for key in d:
	if d[key] == max_count:
				print(key, ":", d[key])
		
# Q 5
s = "mississippi"
d = {}
for char in s:
	if char in d:
		d[char] += 1
	else:
		d[char] = 1
max_count = 0
for key in d:
	if d[key] > max_count:
		max_count = d[key]
		
for key in d:
	if d[key] == max_count:
		print(key, ":", d[key])
		
# Deeper in dictonaries
#Q 6
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}
for key in student.keys():
	print(key)
for value in student.values():
	print(value)
	
#Q 7
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}
for key, value in student.items():
	print(key, value)	

# Q 8
marks = {
    "math": 90,
    "science": 80,
    "english": 85
}
max_marks = 0
top_subject = ""
for key, value in marks. items():
	if value > max_marks:
		max_marks = value
		top_subject = key
print(top_subject, ":", max_marks)

# Q 9 Advanced level dictonaries
students = [
    {"name": "Rahul", "marks": 90},
    {"name": "Amit", "marks": 80},
    {"name": "Neha", "marks": 95}
]
max_marks = 0
top_student= ""
for student in students:
	if student["marks"] > max_marks:
		max_marks = student["marks"]
		top_student = student["name"]
		
print(top_student, ":", max_marks)

#Q 10
students = [
    {"name": "Rahul", "marks": 90},
    {"name": "Amit", "marks": 80},
    {"name": "Neha", "marks": 95}
]
new_list = []
for student in students:
	if student["marks"] > 85:
		new_student = {
			"name": student["name"],
			"marks": student["marks"]
		}
		new_list.append(new_student)

print(new_list)

#Q 11
students = [
    {"name": "Rahul", "marks": 90},
    {"name": "Amit", "marks": 80},
    {"name": "Neha", "marks": 95}
]
new_list = []
for student in students:
	if student["marks"] > 85:
		new_list.append(student["name"])
print(new_list)

# Mini Project
students = [
    {"name": "Rahul", "marks": 90},
    {"name": "Amit", "marks": 80},
    {"name": "Neha", "marks": 95}
]
pass_fail_list =[]
for student in students:
	if student["marks"] >= 85:
		status = "pass"
	else:
		status = "fail"
		
	new_list = {
		"name" : student["name"],
		"status" : status
	}
	pass_fail_list.append(new_list)
print(pass_fail_list)