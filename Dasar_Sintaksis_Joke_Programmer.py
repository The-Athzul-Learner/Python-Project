"""
Semua sintaksis dasar terdiri dari:
1. Sequensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali kali sampai kondisi terpenuhi
"""
# Sequensial
print('Ibu memberi perintah,"Pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus dilakukan di toko?"')
print('Ibu menjawab,"Beli satu botol susu, jika ada telur bawa 6"')
print("Maka Budi berangkat ke toko ")
print("Dan mulai berbelanja")

# Percabangan
print("Budi mengecek apakah susu tersedia")
jumlah_susu=3
jumlah_telur=0
if jumlah_susu > 0:
    print("Susu tersedia")
    print("Budi mengecek apakah telur tersedia")
    if jumlah_telur > 0:
        print("telur tersedia")
        print("Budi membeli 1 susu dan 6 telur")
    else:
        print("telur tidak tersedia")
        print("Budi hanya membeli 1 susu")
else:
    print("Susu tidak tersedia")
    print("Budi tidak jadi membeli susu")
print("Budi pulang ke rumah")









