#Assignment 9.1 Derek Perry 08/01/2020
import os
print("What is name of the directory you want to save your file to?")
directory = input()
path = ("C:\\Users\\derek\\OneDrive\\Documents\\" + directory)
print("What would you like to name the file?")
file_name = input()
if os.path.isdir(directory):
  print("The directory has been found!")
else:
  os.mkdir(path, 777)
print("What is your name?")
user_name = input()
print("What is your current address?")
user_address = input()
print("What is your phone number?")
user_number = input()
user_info = (user_name + ", " + user_address + ", " + user_number)
with open(file_name,'w') as file_write:
  file_write.write(user_info)
with open(file_name, 'r') as file_read:
  file_data = file_read.read()
print(file_data)
