import os

sub_folders = ['tb', 'test', 'sim'] # Variable for proj sub folder names

# -----------------------------------------------
# Function to create directory tree recursively
# -----------------------------------------------
def create_directory_tree (proj_name, depth, max_children):

  if depth <= 0:
    return

  for i in range(max_children):
    # Create subdirectory
    sub_dir = os.path.join(proj_name, sub_folders[i])
    try:
      os.makedirs(sub_dir)
      print(f"Directory '{sub_dir}' created...")
    except FileExistsError:
      print(f"Directory '{sub_dir}' already exists. Skipping...")

    # Recursively call function for subdirectories
    create_directory_tree(sub_dir, depth - 1, max_children)
