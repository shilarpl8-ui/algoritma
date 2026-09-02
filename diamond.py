# tentukan 'n' sebagai setenggah timnggi wajik (tanpa baris tenggah melebat)
# untuk pola di gambar dengan total 11 baris, n = 5
n = 5

# bagian atas ( segitiga biasa - 6 baris)
# perulangan ini mencetak baris 1 sampai 6 ( baris tenggah terlebar)
for i in range(n + 1):
    # cetak sepasi di kiri(berkurang seiring bertambahnya i)
    # n-i menghasilkan 5, 4, 3, 2, 1, 0, spasi
    print(" " * (n - i), end="")
    # cetak bintang ( bertambah ganjil: 1, 3, 5, 9, 7, 11)
    print("*" * (2 * i +1))

# bagian bawag ( segitiga terbalik - 5 baris)
# penggurangan ini mencetak baris 7 sampai 11, mulai dari baris setelah baris tenggah
for i in range(n - 1, -1, -1):
    # cetak spasi di kiri ( bertambah seiring berkurangnya i)
    # n-i menghasilkan 1, 2, 3, 4, 5, spasi
    print(" " * (n-i), end="")
    # cetak bintang (berkurang ganjil: 9, 7, 5, 3, 1)
    print("*" * (2 * i + 1))