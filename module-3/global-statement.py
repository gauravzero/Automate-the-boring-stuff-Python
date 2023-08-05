def spam():
    global eggs # We are telling python that when we use eggs inside this function use the same one that is defined outside, or introduce a global variable
    eggs = 'Hello'
    print(eggs)

def spam2():
    # eggs is global so now anyone can access it
    # global eggs <-- redundant
    eggs = 5
    print(eggs)

eggs = 2
spam()
spam2()
print(eggs)


# Why scope the vars?

# So that if something goes wrong
# due to a wrong value in a var, 
# then we need to investigate 
# the whole program
# With local scope, we can inspect
# only parts of the code