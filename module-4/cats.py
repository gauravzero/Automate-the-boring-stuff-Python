# Allocate 1GB of memory
print("ALLOCATED 1GB")
while True:
    print('How many cats you got?')
    numCats = input()
    try : 
        if int(numCats) < 0 :
            print('Invalid Number of Cats!')
        elif int(numCats) > 3 :
            print('Lot of cats!')
            break
        else : 
            print('Not alot of cats!')
            break
    except ValueError:
        print('Invalid number!Can you enter it again?')


