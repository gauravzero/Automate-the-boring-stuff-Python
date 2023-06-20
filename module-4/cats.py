print('How many cats you got?')
numCats = input()
try : 
    if int(numCats) < 0 :
        print('Invalid Number of Cats!')
    elif int(numCats) > 3 :
        print('Lot of cats!')
    else : 
        print('Not alot of cats!')
except ValueError:
    print('Invalid number!')
