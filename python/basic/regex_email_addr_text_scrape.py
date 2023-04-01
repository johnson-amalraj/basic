import re

# 'WE can give particular word' -> 'Python'
# '[we can give multiple letters]' -> '[abc]'
# '[We can give range]' -> '[a-zA-Z0-9]'
# '[We can give range]+' -> '[a-zA-Z0-9]+' -> it will search multiple letters
# It will search special character also
# '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+' -> it will search email address (A-Z0-9@website.com)

text = 'This is the ReGeX Python Program'
email = 'YourName123@website.com My.-name_123@company.com'

text_pattern = re.compile('[a-zA-Z]+')
email_pattern = re.compile('[a-zA-Z0-9\.\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]+')

result_text = text_pattern.search(text) # It will return only first occurrences
result_email = email_pattern.search(email)
findall_email = email_pattern.findall(email) # It will return all occurrences

print(result_text)
print(result_email)
print(findall_email)