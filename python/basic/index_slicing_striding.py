digits = [2,4,6,2,15,7,32,65,12,78]

print(len(digits))

# Indexing
# We can use negative indexing to print the content in the list
print(digits[-1])
print(digits[-2])
print(digits[-10])
print(digits[-9])

# Slicing
# We can print the content of the list by using range
print(digits[:5])
print(digits[0:5])

print(digits[5:])
print(digits[5:10]) 

print(digits[5:0]) # it prints nothing

print(digits[0:-1])

# Striding
print(digits[0:10:1])
print(digits[0:10:2])
print(digits[0:10:4])

print(digits[::3])

print(digits[10:0:-1])
print(digits[10:0:-2])
print(digits[::-1])
print(digits[::-2])

print()

for i in range (len(digits)):
    print(digits[:i])

print()

for i in range (len(digits)):
    print(digits[i:i+4])

print()
window_size = 4
for i in range (len(digits)-(window_size-1)): 
# Give the windows_size-1 in paranthesis (windows_size-1), else it not correctly working
    print(digits[i:i+window_size])