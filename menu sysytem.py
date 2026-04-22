# Take task
tasks = []
def add_task():
  task = input("enter the task")
  tasks.append(task)
  
  
# View task
def view_task():
  if not tasks:
    print("No tasks available")
  else:
    for i, task in enumerate(tasks, 1):
      print(i, ":", task)
    
# Remove task
def remove_task():
  remove = input("enter task to remove")
  new_list =[]
  
  found = False
  for task in tasks:
    if task != remove:
      new_list.append(task)
    else:
      found = True
  tasks[:] = new_list    
  if found:
    print("deleted sucessfully")
  else:
    print("task not found")
    
#menu system:
while True:
  print("\nchoose operation")
  print("1. Take task")
  print("2. view task")
  print("3. Remove task")
  print("4. Exit")
  
  choice = input("enter the choice")
  if choice == "1":
    add_task()
  elif choice == "2":
    view_task()
  elif choice == "3":
    remove_task()
  elif choice == "4":
    print('exiting')
    break
  else:
    print("Invalid choice")
