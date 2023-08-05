# creating a file and assigning the fd
import os,time

fd = open("meow.txt","w")
fd.write("test")

for x in range(4):
    print("Seconds passed are ", x)
    time.sleep(1)
try:
    os.remove("meow.txt")
except FileNotFoundError:
    print("File isnt found!")


    
    