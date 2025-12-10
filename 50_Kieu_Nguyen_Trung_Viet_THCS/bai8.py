def tim_so_le_lon_nhat(a, b, c):
    lon_nhat = -1 
    if a % 2 == 1 and a > lon_nhat:
        lon_nhat = a
    if b % 2 == 1 and b > lon_nhat:
        lon_nhat = b
    if c % 2 == 1 and c > lon_nhat:
        lon_nhat = c

    return lon_nhat
print(tim_so_le_lon_nhat(1,2,3))