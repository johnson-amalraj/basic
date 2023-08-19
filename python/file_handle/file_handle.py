# program to write/read new files
import os;

# opening filr in read mode
file = open("content.txt", "r")
# printing content of the file
print(file.read())



# closing the file
file.close()
