# AIM: Task List Manager
# Coder:Shamal 
# Date:26/01/26

# Original task list
tasks = ['Sleep', 'Getup', 'Brush']
print("Original Tasks:", tasks)

# --- Add Task ---
new_task = input("Enter a new task to add: ")
tasks.append(new_task)
print("Tasks after Adding:", tasks)

# --- Edit Task ---
edit_index = int(input("Enter the index of the task to edit: "))
new_value = input("Enter the new task: ")
tasks[edit_index] = new_value
print("Tasks after Editing:", tasks)

# --- Remove Task ---
remove_index = int(input("Enter the index of the task to remove: "))
tasks.pop(remove_index)
print("Tasks after Removing:", tasks)

# --- Sort Tasks ---
tasks.sort()
print("Tasks after Sorting:", tasks)




