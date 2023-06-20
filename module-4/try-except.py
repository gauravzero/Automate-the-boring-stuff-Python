# Today getting an error or exception in the program results in a crash

# Try Except enables us to handle such errors and exceptions

# This is used for input validation 

def div42by(divideBy):
    try :
        return 42/divideBy
    except ZeroDivisionError:
        print('Error : You tried to divide by Zero!')

print(div42by(2))
print(div42by(12))
print(div42by(0))