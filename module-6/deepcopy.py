import copy

tester = ['1','2','3','4']
copiedlist = copy.deepcopy(tester)
print(copiedlist)
copiedlist.append('5')
print("og list : " , tester)
print("new list : " , copiedlist)
