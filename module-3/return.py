# Function calls can be part of expressions since they evaluate to the value returned by the function

def printlengthOfString(myString):
    print(len(myString))
    return 1

x = printlengthOfString('tester')
print('Return value of the function is ' + str(x))