import include

def main():
  proj_name = str(input("Enter the project name: ")) # Variable for proj name
  
  # Create directory tree with a depth of 1 and maximum 3 children per directory
  include.create_dir_struct(proj_name, 1, 3)
  
  # Create files inside the each folder
  include.create_files(proj_name)
  
  # Print tree command output
  include.print_dir_struct("tree")

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
