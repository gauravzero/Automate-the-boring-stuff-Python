# Today getting an error or exception in the program results in a crash

# Try Except enables us to handle such errors and exceptions

# This is used for input validation 

def div42by(divideBy):
    try :
        return 42/divideBy # By default its return type is
    except ZeroDivisionError:
        print('Error : You tried to divide by Zero!')
    except TypeError:
        print('Error : Unsupported Type MAN!')
        return 42//2

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by("me"))

# # OUTPUT : 
# 21.0
# 3.5
# Error : You tried to divide by Zero!
# None
# Error : Unsupported Type MAN!
# None