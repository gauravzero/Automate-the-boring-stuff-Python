def eggs(someparameter):
    someparameter.append('yo')

spam = [1,2,3]
eggs(spam)
print(spam)

# Lists of mutable references 

# When this is passed to the eggs function, its passing the reference since its a mutable reference. 
# If it was immutable, this would not occur

# Although someparameter is being passed, and the local scope copy is made - that is of the reference. But it points to the original data. Hence, even after the local var is destroyed, the original reference is still present

# Python is designed like this so that its easy to pass large list references. If we were passing the gigantic list each time, it would be computationally expensive