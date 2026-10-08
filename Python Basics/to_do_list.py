to_do_list = ["Learn Web Dev", "Study DSA","Learn Agentic AI"]

#Adding task to the list
to_do_list.append("Workout")
to_do_list.append("Attend Classes")

##Removing a completed task
to_do_list.remove("Study DSA")

# Checking if a task is in the list
if "Learn Web Dev"  in to_do_list:
    print("Don't forget to Learn web dev")

print("To Do List remaining")
for task in to_do_list:
    print(f"-{task}")
