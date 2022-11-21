"""
Program Perulangan Membaca Buku dengan While
"""
#Tanpa Pembatas
print('Ibu memberi perintah,"Baca dan pahami semua bukumu!"')
jumlah_buku=13
read_and_understood_book=0
jumlah_baca=0
print(f"Jumlah buku saya {jumlah_buku}")
print(f"Jumlah buku yang di baca dan dipahami {read_and_understood_book+1}")
while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if read_and_understood_book==12:
        print(f"Buku ke {read_and_understood_book} belum paham")
    else:
        read_and_understood_book = read_and_understood_book + 1
        print(f'Buku ke {read_and_understood_book+1} sudah dibaca dan dipahami')
print(f'Jumlah buku yang sudah dibaca dan dipahami {read_and_understood_book}')
if read_and_understood_book==jumlah_buku+1:
    print("Bu, Semua buku sudah dibaca dan dipahami")
else:
    print("Bu, tidak semua buku bisa dibaca dan dipahami")


print("selesai")

