"""
Program Perulangan Membaca Buku dengan While
"""
print('Perintah Ibu,"Baca semua bukumu!"')
jumlah_buku = 100
print(f"Jumlah buku {jumlah_buku}")
jumlah_buku_yang_sudah_dibaca=0

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")
print("selesai")