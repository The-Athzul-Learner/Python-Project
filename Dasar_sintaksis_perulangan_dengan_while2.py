"""
Program Perulangan Membaca Buku dengan While
"""
print('Ibu memeberi perintah,"Baca semua bukumu!"')
mybook=13
read_book=0
print(f"Jumlah buku saya : {mybook}")
while read_book < mybook:
    read_book = read_book+1
    print(f"Buku ke {read_book} sudah dibaca")
print("Selesai")

