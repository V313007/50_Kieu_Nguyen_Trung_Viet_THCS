#nhập tổng kẹo và só hs
tong_keo = int(input("Tổng số kẹo là : "))
so_hoc_sinh = int(input("Số học sinh là :"))

#tính số kẹo mỗi hs nhận dc và kẹo thừa
keo_hs_nhan_duoc = tong_keo // so_hoc_sinh
keo_thua = tong_keo % so_hoc_sinh

#in ra
print(f"Số kẹo mỗi học sinh nhận được là : {keo_hs_nhan_duoc} cái" )
print(f"Số kẹo còn thừa là : {keo_thua} cái")