open("tasks.txt", "a").close()
# Task manager
def add_task(task_name):
  with open("tasks.txt", "a") as file:
    file.write(f"{task_name},pending\n")
  print("task added")
  
def view_task():
  with open("tasks.txt", "r") as file:
    for line in file:
      task, status = line.strip().split(",")
      print("Name", task, "|status",status)
      
def mark_done():
  task_name = input("enter the task name")
  new_data =[]
  found = False
  with open("tasks.txt", "r") as file:
    for line in file:
      task, status = line.strip().split(",")
      if task.lower() == task_name.lower():
        status = "done"
        found = True
      new_data.append(f"{task},{status}\n")
  
  with open("tasks.txt","w") as file:
    for line in new_data:
      file.write(line)
      
  if found:
    print("task marked as done")
  else:
    print("task not found")
    
# Delete task
def delete(delete_task):
  choice = input("Are you sure to delete, (Yes/No):")
  if choice.lower() != "yes":
    print("deleted cancelled")
    return
  
  new_list =[]
  found = False
  
  with open("tasks.txt", "r") as file:
    for line in file:
      task, status = line.strip().split(",")
      
      if task.lower() != delete_task.lower():
        new_list.append(line)
      else:
        found = True
        
  with open("tasks.txt", "w") as file:
    for line in new_list:
      file.write(line)
      
  if found:
    print("deleted successfully")
  else:
    print("task not found")

#Menu
while True:
  print("\nchoose operations")
  print("1. addtask")
  print("2. view task")
  print("3. Mark task")
  print("4.Delete task")
  print("5. exit")
  
  choice = input("enter the choice")
  if choice == "1":
    task_name = input("enter the task name")
    add_task(task_name)
  elif choice == "2":
    view_task()
  elif choice == "3":
    mark_done()
  elif choice == "4":
    delete_task = input("enter the name of task which you want to delete")
    delete(delete_task)
  elif choice == "5":
    print("exiting")
    break
  else:
    print("invalid choice")
    
        
    