# ===================================================
# Berkas: main.py
# Deskripsi: Program utama untuk menguji modul math_operations
# ===================================================

# Cara 1: Mengimpor seluruh modul utuh
import math_operations

# Cara 2: Mengimpor fungsi spesifik langsung ke namespace
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

print("=" * 50)
print("--- UJI COBA MODUL MATEMATIKA (PENGGUNAAN) ---")
print("=" * 50)

# 1. Uji Geometri (Persegi)
print("\n1. BANGUN DATAR PERSEGI (Sisi = 5)")
print(f"   Luas     : {math_operations.luas_persegi(5)}")
print(f"   Keliling : {math_operations.keliling_persegi(5)}")

# 2. Uji Geometri (Persegi Panjang)
print("\n2. BANGUN DATAR PERSEGI PANJANG (P=8, L=4)")
print(f"   Luas     : {math_operations.luas_persegi_panjang(8, 4)}")
print(f"   Keliling : {math_operations.keliling_persegi_panjang(8, 4)}")

# 3. Uji Geometri (Lingkaran)
print("\n3. BANGUN DATAR LINGKARAN (r = 7)")
print(f"   Luas     : {math_operations.luas_lingkaran(7):.2f}")
print(f"   Keliling : {math_operations.keliling_lingkaran(7):.2f}")

# 4. Uji Konversi Suhu
suhu = 30
print(f"\n4. KONVERSI SUHU ({suhu} derajat Celsius)")
print(f"   Ke Fahrenheit : {celsius_ke_fahrenheit(suhu):.2f} F")
print(f"   Ke Kelvin     : {celsius_ke_kelvin(suhu):.2f} K")

print("\n" + "=" * 50)
print("Selesai!")