"""List Comprehension"""
# Biasa dipakai di django

# del cara makenya beda, dia dipake di depan
print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# [:] list comprehension -> (start dari mana):(end di mana)
print('\nPerintah del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension dengan start dan end')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
# index dimulai dari 0 tapi elemen tetap dari 1
del daftar_buku[0:-1] # start:end # minus dari belakang
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension dengan start dan end dan step')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX', 1, 2, 3, 4, 5, 6, 7, 8]
del daftar_buku[0::3] # start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat daftar buku baru')
daftar_buku = ['Seven Habits', 'How to Influance People', 'First Things First', '4DX']
daftar_buku_baru = daftar_buku[:] # mesti pake list comprehension disini
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension: ambil yang ganjil')
daftar_buku = ['1 Seven Habits', '2 How to Influance People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ambil yang genap')
daftar_buku = ['1 Seven Habits', '2 How to Influance People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: buang yang ujung')
daftar_buku = ['1 Seven Habits', '2 How to Influance People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ambil yang ganjil')
daftar_buku = ['1 Seven Habits', '2 How to Influance People', '3 First Things First', '4 4DX']
print(daftar_buku[0::2])
