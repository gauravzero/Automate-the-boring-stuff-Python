#With elif statements, the order does matter. Execution enters the first block it satisfied
# else block can be added if you want to execution to enter that section when no other conditions are satisfied

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice')
elif age >2000 :
    print('Alice is not a vampire')
elif age >100 :
    print('Alice is not a grandma')