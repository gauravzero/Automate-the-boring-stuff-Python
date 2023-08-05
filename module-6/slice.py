# A slice has 2 indices in it, seperated by a colon

spam = ['cat', 'rat', 'elephant']
spamSlice = spam[1:2]

# slices evaluate to a new list value
# slice[x:y] is including xth element,
# until but not including yth element
print(spamSlice)

# setting all values in slice to something
spamSlice = spam[1:3]
spamSlice = ['CAT', 'DOG', 'ELEPHANT']
print(spamSlice)

# slice without the index means it either includes the
# beginning or the end of the list, or even both

fullSlice = spam[:]
print(fullSlice)

