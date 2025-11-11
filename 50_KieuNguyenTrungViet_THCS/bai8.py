#nhập cn va ccao
can_nang = float(input("Nhập cân nặng (kg):"))
chieu_cao = float(input("Nhập chiều cao (m):"))

#tính BMI
BMI = can_nang / (chieu_cao * chieu_cao)

#in 
print(f"Kết quả BMI : {BMI:.2f}")