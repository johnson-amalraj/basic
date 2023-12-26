import include

proj_name   = str(input("Enter the project name: ")) # Variable for proj name

# Create directory tree with a depth of 1 and maximum 3 children per directory
include.create_directory_tree(proj_name, 1, 3)
