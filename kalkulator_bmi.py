# Kalkulator BMI

berat = int(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Menghitung BMI
bmi = berat / tinggi ** 2

print(bmi)

# Menentukan kategori
if bmi <= 18.5:
    Kategori=("Kurus (Underweight)")
if bmi <= 18.5:
    Kategori=("Normal (Ideal)")
if bmi <= 25.5:
    Kategori=("Gemuk (Overweight)")
print(f"kategori (kategori).")