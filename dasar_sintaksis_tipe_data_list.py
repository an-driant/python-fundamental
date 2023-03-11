daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

# \n untuk new line atau seperti nekan "Enter"
print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

# [] : ke-(sekian)
print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

# len : panjangnya sesuatu
print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# .append menambahkan elemen di paling ujung
print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']

print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# clear list untuk menghapus isi variabel
print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# .pop mengambil elemen dari list dan kita bisa meletakkanya
# Langsung dimasukin variabel baru sambil diambil
print('\nMengambil buku ke-2')
buku_yang_diambil = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku_yang_diambil)

# .pop tanpa parameter '(0)' -> '()' akan mengambil yang paling ujung
print('\nPop :')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# .pop parameter minus dimulai dari ujung
print('\nPop :')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
