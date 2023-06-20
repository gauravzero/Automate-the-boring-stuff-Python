#Global Scope
# Created when program is created. Destroyed when program exists
spam = 42
def eggs():
    # Local Scope
    # Created when function is called. When returned, the local scope vars are destroyed
    spam = 34
    print(spam)

# def eggs2():
#     print(spam1)

print('Code here!')
print(spam)
eggs()

# Variable cant be local and global