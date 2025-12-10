def giai_phuong_trinh_bac_nhat (a,b):
    if a == 0 :
        if b == 0:
            print("Phương trình vô số nghiệm")
        else :
            print("Phương trình vô nghiệm")
    else:
        x = -b/a
        print("Nghiệm của phương trình là :", x)

print(giai_phuong_trinh_bac_nhat(2,4))
print(giai_phuong_trinh_bac_nhat(4,0))
print(giai_phuong_trinh_bac_nhat(0,6))