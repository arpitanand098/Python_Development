### Read a whole file
with open('python.txt', 'r') as file:
   content = file.read()
   print(content)

## Read a file line by line
with open('python.txt', 'r') as file:
   for line in file:
      print(line.strip()) # strip() removes the newline Character at the end of each line

### Writing A file(Overwriting)
with open('python.txt', 'w') as file:
   file.write("Hello, World!!\n")
   file.write("This is a new line.")

### Write a file(wwithout Overwriting)
with open("python.txt", "a") as file:
   file.write("\nThis will be appended to the file.\n")

## Writing List of lines to a file
lines = ['line 1\n', 'line 2\n', 'line 3\n']
with open('python.txt', 'a') as file:
   file.writelines(lines)

## Writing and then reading a file
with open('python.txt', 'w+') as file:
   file.write("This a text file.\n")
   file.write("This is a new line \n")

   ## Move the file cirsor to the begining
   file.seek(0)

   ## Read the content of the file
   content = file.read()
   print(content)