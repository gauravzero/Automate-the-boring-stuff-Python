import pprint
letters={}
print("enter")
yourname = input()
for char in yourname.lower():
    print(type(char))
    # initialize found letter to zero 
    # if found

    letters.setdefault(char,0)

    # These lines are the longer way to do 
    # it without setdefault

    # if char not in letters:
    #     letters[char]=0 

    letters[char] = (letters[char])+1
print(letters)

pprint.pprint(letters) # Pretty print of dictionary