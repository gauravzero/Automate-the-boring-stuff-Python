name = 'yodel'
# treating a string as a list of character
print(name[:])

for letter in name :
    print(letter)

# Strings in python are immutable
# To modify them, create a new
# string using the slice operator

newName = name[2:3]+"woot"
name += "yolo"
print(newName)
print(name)

# Rule : name internally cant be changed
# name <- 0x0000 to 0x0003 included

# tempname = name + "yolo"
# tempname <- 0x0004 to 0x00012 included
# name address = tempname address
# now name is pointing to tempname




