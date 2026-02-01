# AIM: Task List Manager
# Coder:Shamal 
# Date:26/01/26

print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# Adding a new task
new_task = input("Enter the new task to add:")
tasks.append(new_task)
print("Tasks after adding:", tasks)

#Editing a task
edit_index = int(input("Enter the index of the task to edit:"))
new_task_name = input("Enter the new task:")
tasks[edit_index] = new_task_name 
print("Task after Editing:", tasks)

#Removing a task
remove_index = int(input("Enter the index of the task to remove:"))
tasks.pop(remove_index)
print("Tasks after Removing:", tasks)

#Sorting tasks
tasks.sort()
print("Tasks after Sorting:", tasks) Write your code here
# TODO: Add & Print new Task from user

# TODO: Edit & Print task selected by User

# TODO: Remove & Print a Task selected by User

# TODO: Sort & Print the Tasks

