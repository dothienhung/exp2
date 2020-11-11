
def compare(x,y):
    if x <y :
        if y%2 ==0 :
            return 1+ compare(x,y/2)
        else:
            return  1+ compare(x,y +1)
    else:
        return 0


result = compare(4,11)
print("Ket qua là :", result)




    

