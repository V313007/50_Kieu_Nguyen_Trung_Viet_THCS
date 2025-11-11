#nhập số tiền
so_tien = float(input("Nhập số tiền (VND) :"))

#chuyển đổi số tiền
ty_gia = 24500
chuyen_doi_tien = so_tien / ty_gia

#in
print(f"Số tiền sau khi đổi là : {chuyen_doi_tien:.2f} USD")