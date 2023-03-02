"""
Program perulangan membaca buku dengan for
"""
jumlah_buku = 100
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah buku yang sudah dibaca : {jumlah_buku_yang_sudah_dibaca}")

for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Membaca buku ke-{jumlah_buku_yang_sudah_dibaca}")

print(f"Jumlah buku yang sudah dibaca : {jumlah_buku_yang_sudah_dibaca}")
