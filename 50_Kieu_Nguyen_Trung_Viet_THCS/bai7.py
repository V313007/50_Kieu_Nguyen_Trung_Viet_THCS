def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    
    for n in range(a, b + 1):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        if s == n:
            tong += n
    
    return tong

print(tinh_tong_so_hoan_hao(1,100))