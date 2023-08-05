import os
x=0
print(os.getcwd())
for mydirPath, mydirNames, myFilenames in os.walk(os.getcwd()):
#   single element,    list,   list
    x=x+1
    print("ITERATION : ", x)
    print(mydirPath)
    for name in mydirNames:
        print(name)
    for file in myFilenames:
        print(file)
