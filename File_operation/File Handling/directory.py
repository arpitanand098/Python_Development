## Create a new directory
import os
new_directory = "package"
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' created Successfully.")

## listing Files and directories
items = os.listdir('.')
# print(items)

## Joining Paths

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name, file_name)
# print(full_path)

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(),dir_name, file_name)
print(full_path)

## Checking if a path exists
path = 'python1.txt'
if os.path.exists(path):
    print(f"The path '{path}' exists")
else:
    print(f"The path '{path}' does not exist")

## Checking if a path is a file or Directory
import os 
path = 'file.py'
if os.path.isfile(path):
    print(f"The path '{path}' is a file.")
elif os.path.isdir(path):
    print(f"The path '{path}' is a directory.")
else:
    print(f"The path '{path}' is neither a directory nor a file.")

## Getting the absolute path
relative_path ='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)

new_directory = "Exception Handling"
os.mkdir(new_directory)
print(f"Directory '{new_directory}' created successfully.")