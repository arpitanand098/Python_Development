import re

pattern = r'\d+'
text = 'There are 2 peoples'
match = re.search(pattern,text)
print(match.group())