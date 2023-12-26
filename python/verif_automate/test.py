import os

# print ("automate file")

# Define folder names
folders = ['folder1', 'folder2', 'folder3']

# Create folders
for folder_name in folders:
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")

# Define file names and their content
files_info = {
    'folder1': ['file1.txt', 'Hello from file1!'],
    'folder2': ['file2.txt', 'Greetings from file2!'],
    'folder3': ['file3.txt', 'Content for file3.']
}

# Create files in respective folders
for folder, (file_name, content) in files_info.items():
    file_path = os.path.join(folder, file_name)
    with open(file_path, 'w') as file:
        file.write(content)

print("Files created in respective folders.")

# Listing directories and files in the current directory
for root, dirs, files in os.walk('.'):
    print(f"Directory: {root}")
    for file in files:
        print(f" - File: {file}")


# That sounds like a great plan! Python is a versatile language and can be used effectively for automating VLSI verification testbenches. 
# Here are some steps and tools you might find helpful in automating this process:
# 
# 1. Selecting a Framework: Consider using frameworks like 
#      [Universal Verification Methodology (UVM)](https://en.wikipedia.org/wiki/Universal_Verification_Methodology) or 
#      [SystemVerilog](https://en.wikipedia.org/wiki/SystemVerilog) for verification. 
#    Python can be used to interact with these methodologies through various libraries and interfaces.
# 
# 2. Python Libraries: Python has several libraries that can assist in automation, such as:
#      - pySV:   A SystemVerilog interface for Python.
#      - cocotb: Allows you to write testbenches in Python and interface with Verilog/SystemVerilog.
#      - VUnit:  A unit testing framework for VHDL/SystemVerilog that can be integrated with Python.
# 
# 3. Understanding the Verification Environment: 
#    Get familiar with the existing verification environment and the tools used. 
#    This includes understanding the testbench architecture, stimulus generation, and results collection.
# 
# 4. Integration: Python can serve as a scripting language to automate the execution of simulations, parsing results, and running various test cases. 
#    You can use it to call simulators like Questa, VCS, or ModelSim, and manage the simulation flow.
# 
# 5. Data Processing and Visualization: Python excels in data processing and visualization. 
#    You can use libraries like NumPy, Pandas, and Matplotlib to analyze simulation results, generate plots, and extract meaningful insights from your verification data.
# 
# 6. Continuous Integration/Continuous Deployment 
#    (CI/CD): Incorporate your verification automation into CI/CD pipelines using tools like Jenkins or GitLab CI. 
#             This ensures automated testing with every change in your design.
# 
# 7. Documentation and Reporting:
#    Leverage Python to generate automated reports summarizing test results, coverage metrics, and verification progress.
# 
# Remember, while Python is powerful, its integration with VLSI verification may involve learning specific interfaces and methodologies. It might be helpful to refer to documentation, forums, and communities dedicated to VLSI verification and the tools you are using.
# 
# Would you like more specific information or guidance on any particular aspect of automating the VLSI verification testbench with Python?


# # Define the SystemVerilog file content
# system_verilog_code = '''
# module my_module;
# 
#   // Input and output ports
#   // ... define module ports ...
# 
#   // Module logic
#   // ... insert your module code ...
# 
#   initial begin
#     // Initialize signals or perform initial operations
#     $display("SystemVerilog module initialized");
#     // ... additional initialization ...
# 
#     // Module functionality
#     // ... add module functionality ...
# 
#     // Finish simulation
#     $display("SystemVerilog module finished");
#     $finish;
#   end
# 
# endmodule
# '''
# 
# # Write the generated SystemVerilog content to a file
# with open('my_module.sv', 'w') as file:
#     file.write(system_verilog_code)
# 
# print("SystemVerilog file 'my_module.sv' created successfully.")
