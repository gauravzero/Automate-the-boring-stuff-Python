# Function calls can be part of expressions since they evaluate to the value returned by the function

def printlengthOfString(myString):
    print(len(myString))
    return 1

x = printlengthOfString('tester')

mystr = 'Return value of the function is ' + str(x)

mystr = mystr + "meow"
print(mystr)
print('Return value of the function is ' + str(x))
print('Return value of the function is ',x)