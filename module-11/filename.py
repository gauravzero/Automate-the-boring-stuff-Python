import os
print(os.getcwd())
os.chdir("../")
print(os.getcwd())
print(os.path.abspath('test.png'))

print(os.path.dirname(os.getcwd()))

print("Size of c: is",os.path.getsize('c:\\'))