"""
Semua sintaksis dasar terdiri dari:
1. Sequensial : Langkah mengulang
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali kali sampai konddisi terpenuhi
"""
# Sequensial
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus dilakukan di toko?"')
print('Ibu menjawab,"Beli satu botol susu, jika ada telur bawa 6"')
print("Maka Budi berangkat ke toko ")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 6
jumlah_telur = 0
print(f"jumlah botol susu:{jumlah_botol_susu}")
print(f"jumlah telur:{jumlah_telur}")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata cukup")
    if jumlah_telur > 0:
        print("Budi membeli 1 botol susu dan 6 butir telur")
    else:
        print("Budi membeli 1 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")







