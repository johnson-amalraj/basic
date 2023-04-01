s = "Python. language. tutorial"
# s = 'Python language tutorial'

print(s)
print(s[3])
print(s[:6])
print(s[0:6])

print(s.upper())
print(s.isupper())

print(s.lower())
print(s.islower())

print(s.replace('tutorial', 'programs'))
print(s.replace('t', 'S', 2)) # last parameter how many times replacing takes place

print(s.split('.'))
print(s.split(' '))