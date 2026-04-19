students = [
    {"name": "Rahul", "marks": 90},
    {"name": "Amit", "marks": 80},
    {"name": "Neha", "marks": 95},
    {"name": "Riya", "marks": 70}
]
def pass_fail(students):
  result = [] 
# Pass and Fail
  for student in students:
    if student["marks"] >= 85:
      status= "pass"
    else:
      status = "fail"
    result.append({
    "name" :  student["name"],
    "result" : status
    })
  return result
# Topper
def topper(students):
  max_marks = students[0]["marks"]
  topper = students[0]["name"]
  for student in students:
    if student["marks"] > max_marks:
      max_marks = student["marks"]
      topper = student["name"]
  return topper, max_marks

#Average marks
def average(students):
  total = 0
  for student in students:
    total += student["marks"]
  return total / len(students)

#Above average
def above_average(students, average_marks):
  above_average = []
  for student in students:
    if student["marks"] > average_marks:
      above_average.append(student["name"])
  return above_average

pass_fail = pass_fail(students)
topper, max_marks = topper(students)
average_marks = average(students)
above_average = above_average(students, average_marks)

 
print("pass_fail =", pass_fail)
print("topper =",topper,":",max_marks)
print("average =", average_marks)
print("above_average =", above_average)