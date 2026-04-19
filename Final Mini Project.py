users = [
    {"name": "Rahul", "age": 21, "active": True},
    {"name": "Amit", "age": 17, "active": False},
    {"name": "Neha", "age": 23, "active": True},
    {"name": "Riya", "age": 16, "active": False}
]
# Active users
def active(users):
  list_active = []
  for user in users:
    if user["active"] == True:
      list_active.append(user["name"])
  return list_active

# Adult users
def adult(users):
  list_18 = []
  for user in users:
    if user["age"] >= 18:
      list_18.append(user)
  return list_18

# count Active users:
def count(users):
  count_active = 0
  for user in users:
    if user["active"]==True:
      count_active += 1
  return count_active
  
# create summary
def summary(users):
  total_users    = 0
  active_users   = 0
  inactive_users = 0
  adults         = 0
  for user in users:
    total_users += 1
    if user["active"] == True:
      active_users += 1
    else:
      inactive_users += 1
    if user["age"] >= 18:
      adults += 1
  all_summary = {
    "total_users"   : total_users,
    "active_users"  : active_users,
    "inactive_users" : inactive_users,
    "adults"        : adults
  }
  return all_summary

list_active = active(users)
list_18     = adult(users)
count_active = count(users)
all_summary = summary(users)

print("active_users =", list_active)
print("adults =", list_18)
print("count_active =", count_active)
print("summary =", all_summary)