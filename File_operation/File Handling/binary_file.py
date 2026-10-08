## Writing A binary file
data = b'\x00\x01\x02\x03\x04'
with open('python.bin', 'wb') as file:
    file.write(data)

## Reading a binary file
with open('python.bin', 'rb') as file:
  content = file.read()
  print(content)

###Read the content from the source text file and write it to a destination text file
## Copying a text file
with open('python.txt', 'r') as source_file:
   content = source_file.read()

with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)