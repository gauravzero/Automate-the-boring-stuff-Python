spam = ['meow', 'meow']
print(spam.index('meow'))

spam.append('meow2')
print(spam)

spam.remove('meow')
print(spam)

# Remove will remove the first value it finds from the list

spam.append('yodel')
spam.append('1')
spam.append('&')
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

# Sort uses ASCII-betical order
# Uppercase before lowercase
# Symbols first and numbers next, then letters

spam.sort(key=str.lower)
print(spam)