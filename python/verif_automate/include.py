import os
import subprocess

from datetime import datetime

sub_folders = ['tb', 'test', 'sim'] # Variable for proj sub folder names

current_time = datetime.now()
format_time  = current_time.strftime("%d-%h-%Y %I:%M:%S %p")

# -----------------------------------------------
# Function to create directory tree recursively
# -----------------------------------------------
def create_dir_struct (proj_name, depth, max_children):

  if depth <= 0:
    return

  # Create subdirectory
  for i in range(max_children):
    sub_dir = os.path.join(proj_name, sub_folders[i])
    try:
      os.makedirs(sub_dir)
      print(f"Directory '{sub_dir}' created...")
    except FileExistsError:
      print(f"Directory '{sub_dir}' already exists. Skipping...")

    # Recursively call function for subdirectories
    create_dir_struct(sub_dir, depth - 1, max_children)

# -----------------------------------------------
# Function to create a file inside a specific directory
# -----------------------------------------------
def create_file_in_directory(proj_name, directory_path, file_name):

  proj_name = proj_name.upper()

  try:
    # Change the working directory to the specified directory
    os.chdir(directory_path)

    # Create the file and write top_banner to it
    with open(file_name, 'w') as file:
      top_banner  = f'''// ----------------------------------------------------              
// Project name  : {proj_name}
// File name     : {file_name}
// Author        : Johnson Amalraj [johnsonamalraj@outlook.com]
// Date Added    : {format_time}
// Date Modified : 
// Description   : This is the {file_name} file
// ----------------------------------------------------'''
      file.write(top_banner)
      print(f"File '{file_name}' created in '{directory_path}'.")
  except FileNotFoundError as e:
    print(f"Directory '{directory_path}' not found: {e}")
  except PermissionError as e:
    print(f"Permission error while creating the file: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")

  directory_path = '../../'
  # Change the working directory to the specified directory
  os.chdir(directory_path)

# -----------------------------------------------
# Function to create a file inside a tb directory
# -----------------------------------------------
def create_tb_folder_files (proj_name):

  # tb folder files
  directory_path = f'{proj_name}/tb'
  file_names     = ['top.sv', 'interface.sv', 'env.sv', 'checker.sv', 'base_test.sv', 'common_sequence', 'mst_agent.sv', 'mst_driver.sv', 'mst_sequencer.sv', 'mst_monitor.sv', 'slv_agent.sv', 'slv_driver.sv', 'slv_sequencer.sv', 'slv_monitor.sv']

  for file_name in file_names:
    create_file_in_directory(proj_name, directory_path, file_name)

# -----------------------------------------------
# Function to create a file inside a test directory
# -----------------------------------------------
def create_test_folder_files (proj_name):

  # test folder files
  directory_path = f'{proj_name}/test'
  file_name      = 'test_basic.sv'

  create_file_in_directory(proj_name, directory_path, file_name)

# -----------------------------------------------
# Function to create a file inside a sim directory
# -----------------------------------------------
def create_sim_folder_files (proj_name):

  # sim folder files
  directory_path = f'{proj_name}/sim'
  file_names     = ['run.f', 'Makefile']

  for file_name in file_names:
    create_file_in_directory(proj_name, directory_path, file_name)

# -----------------------------------------------
# Function to create a files inside all directories
# -----------------------------------------------
def create_files (proj_name):

  create_tb_folder_files(proj_name)
  create_test_folder_files(proj_name)
  create_sim_folder_files(proj_name)

# -----------------------------------------------
# Function to print tree structure
# -----------------------------------------------
def print_dir_struct (command):
  
  # Execute the command using subprocess
  process       = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  # Capture the output and error
  output, error = process.communicate()
  
  # Decode the byte strings to UTF-8
  output_str = output.decode("utf-8")
  error_str  = error.decode("utf-8")

  if error_str.strip() == "":
    # Print the output and error
    print("Folder tree structure:", output_str)
  else:
    print("Error:", error_str)
