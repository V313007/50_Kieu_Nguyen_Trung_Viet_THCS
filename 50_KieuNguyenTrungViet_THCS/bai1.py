#nhập giá sp và số lượng mua
gia_san_pham= float(input("Nhập giá sản phẩm (VND): "))
so_luong_mua = int(input("Nhập số lượng mua : "))

#tính tổng chi phí , thuế , tổng tiền
tong_chi_phi = gia_san_pham * so_luong_mua
tien_thue = tong_chi_phi * 0.1
tong_tien = tong_chi_phi + tien_thue

#in ra kq
print(f"Tổng chi phí (chưa tính VAT) : {tong_chi_phi:.2f} VND")
print(f"Thuế (VAT) : {tien_thue:.2f} VND")
print(f"Tổng tiền phải trả : {tong_tien:.2f} VND")