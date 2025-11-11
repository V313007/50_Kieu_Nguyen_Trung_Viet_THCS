#nhập năm
nam = int(input("Nhập một năm :"))

#tính
nam_nhuan = (nam % 400 == 0 ) or ((nam % 4 == 0 ) and ( nam % 100 != 0))

#in
print(f"Đây là năm nhuận : {nam_nhuan}")