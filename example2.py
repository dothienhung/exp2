import math

def compare():
    x = int(input("Nhap gia gia cua X :"))
    y = int(input("nhap gia tri cua Y :"))
    t = math.ceil(math.log2(y/x))
    count =0
    while x!=y and t >= 0 :
        if x*(2**t) >=y :
            count +=1
            print(x)
            break
        else:
            x=(x+1)*2
            print(x)
            t =math.ceil(math.log2(y/x))
            count =count +1
            break

    

compare()


    







    

