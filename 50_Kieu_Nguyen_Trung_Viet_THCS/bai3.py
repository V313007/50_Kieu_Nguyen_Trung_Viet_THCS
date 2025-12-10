def kiem_tra_so_armstrong(n) :
    tong = 0 
    so = n
    while so > 0 : 
        chu_so = so % 10
        tong = tong + chu_so**3
        so = so // 10 
    return tong ==  n 
print(kiem_tra_so_armstrong(100))
print(kiem_tra_so_armstrong(153))