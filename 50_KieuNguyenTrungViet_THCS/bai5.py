#nhập tiền gửi bđ
tien_gui = float(input("Nhập số tiền gửi (VND) : "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))

#số tiền lãi
i = lai_suat_nam / 100
lai_1_thang = tien_gui * i * (1 / 12) #1/12 năm
lai_2_quy = tien_gui * i * (6 / 12)
lai_3_nam = tien_gui * i * 3 

#in ra
print(f"Tiền lãi nhận được sau 1 tháng là : {lai_1_thang} VND")
print(f"Tiền lãi nhận được sau 2 quý là : {lai_2_quy} VND")
print(f"Tiền lãi nhận được sau 3 năm là : {lai_3_nam} VND")