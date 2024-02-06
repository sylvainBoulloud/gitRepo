import os

print("Hello, this script to create folder in current directory.")
name = str(input("Choose your repo name (must be written in double quotes) : "))
location = os.getcwd()
print(name)
os.mkdir("./"+name)
print(name + " directory created in this location : " + location)
