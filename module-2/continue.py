# continue breaks the execution and returns to the start of the loop

spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3:
        continue
    print('spam is ' + str(spam))