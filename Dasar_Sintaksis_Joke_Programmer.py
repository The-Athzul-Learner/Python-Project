"""
Semua sintaksis dasar terdiri dari:
1. Sequensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali kali sampai kondisi terpenuhi
"""
# Sequensial
print('Ibu memberi perintah,"Pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus dilakukan di toko?"')
print('Ibu memberi perintah,"Beli 1 botol susu, jika ada telur beli 6"')
print('Budi menjawab "Ok"')
print('Budi pergi membeli susu')
# Percabangan
print("Budi mengecek apakah susu tersedia?")
jumlah_susu = 2
jumlah_telur = 6
if jumlah_susu > 0:
    print("Susu tersedia")
    print('Budi mengecek apakah telur tersedia?')
    if jumlah_telur > 0:
        print('Telur tersedia')
        print("Budi membeli 1 botol susu dan 6 telur")
    else:
        print("Budi hanya membeli 1 botol susu")
else:
    print("Budi tidak jadi membeli susu")
print('Budi pulang ke rumah')
print('Budi menyerahkan susu dan telur kepada ibu')
print('Selesai')










