#Nhập tên đăng nhập và mật khẩu
ten_dang_nhap = input("Tên đăng nhập : ")
mat_khau = input("Mật khẩu :")

#ktra quyền truy cập
quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")

#in
print(f"Được phép truy cập {quyen_truy_cap}")