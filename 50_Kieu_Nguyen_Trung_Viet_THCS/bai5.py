def kiem_tra_so_doi_xung(n) :
    so = n
    dao = 0
    
    while so > 0 :
        chu_so = so % 10 
        dao = dao*10 + chu_so
        so = so // 10 
    return dao == n 

print(kiem_tra_so_doi_xung(121))
print(kiem_tra_so_doi_xung(123))