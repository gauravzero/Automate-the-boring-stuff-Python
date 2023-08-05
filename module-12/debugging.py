# Debugging will enable us to find bugs 
# more easily and fix them


def boxPrint(symbol, width, height):
    print('For Height %s and Width %s'%(height, width))
    if height == 0 or width == 0:
        return
    if height == 1 and width == 1:
        print(symbol)
        return
    print(symbol*width)
    for i in range(height-2):
        if width>2:
            print(symbol + ' '*(width-2) + symbol)
        else:
            print(symbol)
    if height-2>=0:
        print(symbol*width)

# for i in range(3):
#     for j in range(3):
#         # print(i,j)
#         boxPrint('*',i,j)

print("Enter height and width and symbol")
h = input()
w = input()
s = input()
boxPrint(s,int(w),int(h))