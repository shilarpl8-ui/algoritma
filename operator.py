print("=== Program Cek Kelulusan ===")

# 1. input() - minimal 1
nilai = int(input("Masukkan nilai ujian: "))
nilai_tugas = int(input("Masukkan nilai tugas: "))

# 2. operator aritmatika - minimal 2
total_nilai = nilai + nilai_tugas      # +
rata_rata = total_nilai / 2            # /

# 3. operator perbandingan - minimal 2
lulus_ujian = nilai >= 75              # >=
lulus_rata = rata_rata >= 70           # >=

# 4. operator logika and dan or
if (lulus_ujian and lulus_rata) or (rata_rata >= 85):
    print("Selamat, Kamu LULUS!")
else:
    print("Maaf, Kamu TIDAK LULUS. Tetap semangat!")

print("--------------------")
print("Total nilai:", total_nilai)
print("Rata-rata:", rata_rata)
print("Lulus ujian >=75:", lulus_ujian)
print("Lulus rata-rata >=70:", lulus_rata)