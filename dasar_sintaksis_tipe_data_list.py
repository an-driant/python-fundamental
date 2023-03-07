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

# nambah buku baru pake .append
print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']

print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
