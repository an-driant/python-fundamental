"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pegi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur maka belilah juga 6 butir telur"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

#  Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"Jumlah susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Apakah ada telur?")
    if jumlah_telur == 0:
        print("Tidak ada")
        print("Budi membeli satu botol susu")
    else:
        print("Telur ada")
        print("Budi membeli 1 botol susu dan 6 butir telur")
else:
    print("Budi bertanya apakah ada telur")
    if jumlah_telur == 0:
        print("Budi tidak membeli apapun")
    else:
        print("Budi hanya membeli 6 butir telur")

print("Budi pulang ke rumah")
print("Budi menyampaikan hasilnya kepada ibu")
