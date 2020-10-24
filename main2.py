# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
#masukan perulangan nilai awal, batas, dan selang 
#yang mau dicetak
for i in range(100, 1, -2):
#akan mencetak hasil perulangan variabel i
    print(i, end="-")
print("\n")
# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
# Membuat variabel untuk menampung banyaknya angka
a = int(input("Masukkan banyaknya angka: "))
# Membuat variabel dengan nilai 0
b = 0
# Perulangan yang diambil dari banyak data
for i in range (a) :
 # Nilai yang akan diinput
    y = eval(input("masukan bilangan bulat: "))
# hasil
    b = b+y / a
 # cetak hasil
print("hasil nilai rata-rata adalah: ",b)
# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

#Akan diberikan sebuah inputan masukan bilangan bulat, yang nanti kemudian akan dibuat bentuk persegi dengan karekter , sesuai dengan jumlah inputan.
#contoh, Jika memasukan angka 9, maka akan tampil karakter dengan kolom dan baris yang sama yaitu 9
bulat = int(input("Masukkan sebuah bilangan bulat: "))
for c in range(bulat):
  print(end='\n')
  for a in range(bulat):
    print('#', end=' ')


