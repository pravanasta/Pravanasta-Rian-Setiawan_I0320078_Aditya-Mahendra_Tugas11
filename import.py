import matematika.geometri2D

# persegi panjang
p = 10
l = 8

luas = matematika.geometri2D.luasPersegiPanjang(p, l)
kel = matematika.geometri2D.kelilingPersegiPanjang(p, l)

print("PERSEGI PANJANG")
print("Panjang\t\t:", p)
print("Lebar\t\t:", l)
print("Luas\t\t:", luas)
print("Keliling\t:", kel)

# lingkaran
jarijari = 3

luas = matematika.geometri2D.luasLingkaran(jarijari)
kel = matematika.geometri2D.kelilingLingkaran(jarijari)

print("\nLINGKARAN")
print("jari-jari\t:", jarijari)
print("Luas\t\t:", luas)
print("Keliling\t:", kel)