# Inisialisasi data awal minimal 3 kontak
buku_kontak = {
    "Andi": "081234567890",
    "Budi": "089876543210",
    "Citra": "082134567890"
}

while True:
    # Tampilkan Menu
    print("\n===== BUKU KONTAK =====")
    print("1. Lihat Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak Baru")
    print("4. Hapus Kontak")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    # a. Lihat Semua Kontak
    if pilihan == "1":
        print("\nDaftar Semua Kontak:")
        for nama, nomor in buku_kontak.items():
            print(f"Nama: {nama}, Nomor HP: {nomor}")

    # b. Cari Kontak pakai .get()
    elif pilihan == "2":
        nama_cari = input("\nMasukkan nama kontak yang dicari: ")
        nomor = buku_kontak.get(nama_cari, "Kontak tidak ditemukan")
        print(f"Nomor HP: {nomor}")

    # c. Tambah Kontak Baru
    elif pilihan == "3":
        nama_baru = input("\nMasukkan nama kontak baru: ")
        nomor_baru = input("Masukkan nomor HP: ")
        buku_kontak[nama_baru] = nomor_baru
        print(f"Kontak '{nama_baru}' berhasil ditambahkan!")

    # d. Hapus Kontak
    elif pilihan == "4":
        nama_hapus = input("\nMasukkan nama kontak yang akan dihapus: ")
        if nama_hapus in buku_kontak:
            del buku_kontak[nama_hapus]
            print(f"Kontak '{nama_hapus}' berhasil dihapus!")
        else:
            print("Kontak tidak ditemukan.")

    # e. Keluar Program
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")