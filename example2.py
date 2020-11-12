
from math import log2

def compare():
    x = int(input("Nhap gia gia cua X :"))
    y = int(input("nhap gia tri cua Y :"))
    count =0

    while (x != y) :
        ntemp = y
        while (x < ntemp) :
            ntemp = ntemp / 2
        
        if (x < ntemp + 1) :
            x = x * 2;
            print("phai nha them :*2")
        else:
            x = x - 1;
            print("phai tru di -1");
        
        count +=1
    
    print("Tong so buoc la: " ,count);
        

compare()


    

  


    







    

