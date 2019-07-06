def lesser(x,y):
    if(x %2 == 0 and y%2 == 0):
        if(x<y):
            return x
        else:
            return y
    elif(x%2 == 0 or y%2 == 0):
        if(x<y):
            return y
        else:
            return x


lesser(10,100)
