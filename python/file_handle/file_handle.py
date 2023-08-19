# program to write/read new files
import os;

# ------------------------------------------------------------------------------------------------------------------------------
# file_object = open('file_name', 'mode')
# ------------------------------------------------------------------------------------------------------------------------------
# mode || description
# ------------------------------------------------------------------------------------------------------------------------------
# 'r'  || reads from a file and returns an error if the file does not exist (default).
# 'w'  || writes to a file and creates the file if it does not exist or overwrites an existing file.
# 'x'  || exclusive creation that fails if the file already exists.
# 'a'  || appends to a file and creates the file if it does not exist or overwrites an existing file.
# 'b'  || binary mode. Use this mode for non-textual files, such as images.
# 't'  || text mode. Use only for textual files (default).
# '+'  || activates read and write methods.
# ------------------------------------------------------------------------------------------------------------------------------

# opening file in write mode
file_obj = open("content.txt", "w")

# this will override the existing content
file_obj.write('first line added\n')

# opening file in read mode
file_obj = open("content.txt", "r")

# printing content of the file
print(file_obj.read())

# opening file in write mode
file_obj = open("content.txt", "w")

# this will override the existing content
file_obj.write('first line overrides\n')

# opening file in read mode
file_obj = open("content.txt", "r")

# printing content of the file
print(file_obj.read())

# opening file in append mode
file_obj = open("content.txt", "a")

# this will append this line at end of the file
file_obj.write('new lines appended\n')

# opening file in read mode
file_obj = open("content.txt", "r")

# printing content of the file
print(file_obj.read())

# closing the file
file_obj.close()

# ------------------------------------------------------------------------------------------------------------------------------
# method	             || description
# ------------------------------------------------------------------------------------------------------------------------------
# close()	             || flushes and closes the file object.
# detach()	             || separates buffer from text stream and returns the buffer.
# fileno()	             || returns the file's descriptor if available.
# flush()	             || flushes the write buffer. Not available for read-only objects.
# isatty()	             || checks if a file stream is interactive.
# read(<int>)	             || read <int> number of characters at most.
# readable()	             || checks if an object is readable.
# readline(<int>)	     || reads from the object until a newline or end of the file.
# readlines(<int>)	     || returns a list of lines from the file object, where <int> is the approximate character number.
# seek(<offset>, <position>) || changes the pointer position to <offset> relative to the <position>.
# seekable()	             || checks if the file object supports random access.
# tell()	             || prints the current stream position.
# truncate(<byte>)	     || resizes the file stream to <bytes> (or current position if unstated) and returns the size.
# write(<string>)	     || writes <string> to the file object and returns the written number of characters.
# writable()	             || checks whether the file object allows writing.
# writelines(<list>)	     || writes a <list> of lines to the stream without a line separator.
# ------------------------------------------------------------------------------------------------------------------------------
