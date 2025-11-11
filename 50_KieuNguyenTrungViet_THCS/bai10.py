luong_co_ban = float(input("Nhập mức lương cơ bản (VND) : "))
ngay_cong = float(input("Nhập số ngày công trong tháng : "))

luong_1_ngay = luong_co_ban / 22
luong_thang = luong_1_ngay * ngay_cong
tien_thuong = 0.1 * luong_thang * (ngay_cong > 22)
tien_phat = 0.05 * luong_thang * (ngay_cong < 22)
tong_tien_luong = luong_thang + tien_thuong - tien_phat

print(f"Lương thực nhận : {tong_tien_luong:.0f} VND")