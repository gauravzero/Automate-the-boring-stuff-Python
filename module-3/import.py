# import random

# # random is the module
# # randint is the function in the module
# # module must be imported

# # multiple modules can be imported
# # by seperating them with commas
# x = random.randint(1,20)
# print(x)


#### OPTIMIZED APPROACH ####

# The order of the functions matter
# If randint is imported after you defined the function with the same name
# then it will override your function and use the library function. Latest takes precendence


from random import randint
def randint(x,y):
    print("you got the randint")
    return

    # It will print None if you print randint(x,y) This is because the return statement without a value simply exits the function and returns None implicitly.
    


x = randint(1,100)
print(x)

print(randint(1,1000))
print("end")