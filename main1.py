# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print ("menghitung rata rata nilai")
nilai1 = int(input("masukan nilai ke-1 "))
nilai2 = int(input("masukan nilai ke-2 "))
nilai3 = int(input("masukan nilai ke-3 "))

totalnilai = nilai1 + nilai2 + nilai3

print("jadi total nilai adalah:", str(totalnilai))
banyaknilai = int(input("masukan banyak nilai: "))
ratarata = totalnilai/banyaknilai
print("jadi rata-ratanya adalah", str(ratarata))


# Si = int(input("Masukkan sebuah bilangan bulat : "))
# Tulikelipatan = int(input("masukkan sebuah bilangan:"))
num = int(input("masukan bilangan bulat "))
print(num*1, num*2, num*3, num*4, num*5, sep= "---")