
def searchKVTupleInDict(tuple, dict):
    for k,v in dict:
        if (k,v) == tuple:
            print("FOUND IT")
            return True
    return False

eggs = {'white':'old','black':'new'}
print(list(eggs.values()))
print(eggs.values())
print("keys:")
print(list(eggs.keys()))
print((eggs.keys()))

# Printing the values of the dict

for val in eggs.values():
    print(val)

# Printing the keys and values of the dict
for key, value in eggs.items():
    print("Key : "+key)
    print("Value : "+value)

this = ('white','old')
print (searchKVTupleInDict(this,eggs.items()))