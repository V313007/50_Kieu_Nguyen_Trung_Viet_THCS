#nhập số kWh điện tiêu thụ
so_kWh = float(input("Nhập số kWh điện tiêu thụ :"))
tien_dien = (so_kWh <= 100) * (so_kWh * 1678)+ ( 100 < so_kWh <= 200) * (so_kWh * 1734) + ( 200 < so_kWh <= 300) * (so_kWh * 2014)

print(f"Tổng tiền điện : {tien_dien} VND ")