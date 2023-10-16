# get the input to be print as banner
logger  = str(input("Enter the logger to format: "))
# get the length of the logger
length  = int(input("Enter the length of the logger: "))
# get the message
message = str(input("Enter the message: "))

#--------------------------------------------------
# definition to print logger (first and last line)
#--------------------------------------------------
def print_logger(logger, length):
   for i in range (length):
     if (i < (length-1)):
       print(logger, end = '')
     else: 
       print(logger)
     
#--------------------------------------------------
# definition to print additional logger (first after and last before lines)
#--------------------------------------------------
def print_add_log():
   for i in range (length):
     if (i == 0):
       print(logger, end = '')
     elif (i == (length-1)):
       print(logger)
     else: 
       print(' ', end = '')

#--------------------------------------------------
# definition to print the original message
#--------------------------------------------------
def print_org_msg(message):
   for i in range (length):
     if (i == 0):
       print(logger, end = '')
     elif (i == (length-1)):
       print(logger)
     else: 
       print(' ', end = '')
       # print(message)
       # TODO: correct the message print with format

#--------------------------------------------------
# definition of main function
#--------------------------------------------------
def main():
   print_logger(logger, length)
   print_add_log()
   print_org_msg(message)
   print_add_log()
   print_logger(logger, length)

#--------------------------------------------------
# call the main function
#--------------------------------------------------
if __name__ == '__main__':
  main()