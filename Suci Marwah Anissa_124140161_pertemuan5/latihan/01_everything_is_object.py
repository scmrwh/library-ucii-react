# 01_everything_is_object.py
# Ngebuktiin kalau di Python semua tipe data itu sebenernya objek

angka = 42
pesan = "Praktikum Pemrograman Web ITERA"
daftar_nilai = [85, 90, 78]

# cek tipe aslinya pakai type()
print("Tipe objek 'angka'        :", type(angka), "| Class:", angka.__class__)
print("Tipe objek 'pesan'        :", type(pesan), "| Class:", pesan.__class__)
print("Tipe objek 'daftar_nilai' :", type(daftar_nilai), "| Class:", daftar_nilai.__class__)

# Ternyata string punya method bawaan sendiri (upper, split)
print("\nManipulasi string via method class str:")
print("Versi Huruf Besar :", pesan.upper())
print("Pecah Kata        :", pesan.split(" "))

# Fungsi juga ternyata objek, punya id memori sendiri
def salam():
    return "Halo dari fungsi!"

print("\nTipe objek fungsi 'salam' :", type(salam))
print("Identitas memori (id)     :", hex(id(salam)))