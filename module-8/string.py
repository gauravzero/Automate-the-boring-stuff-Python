str1 = "The Alice is a \'cat\'"
# when we add the \ it tells python that we dont want to terminate the
# string with the single quote
print(str1)

introstring = "Hello there!\nHow are you?"
print(introstring)

# with the raw string it assumes everything is a part of the string
# without considering escape sequences
rawString = r'carols\n \'cat'
print(rawString)

mlc = '''This
is 
a 
multiline
comment'''
print(mlc)

# strings are like lists

print(mlc[0])
print(mlc[-1])
print(mlc[1:5])