def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 2
spam()
print(eggs)

# Why scope the vars?

# So that if something goes wrong
# due to a wrong value in a var, 
# then we need to investigate 
# the whole program
# With local scope, we can inspect
# only parts of the code