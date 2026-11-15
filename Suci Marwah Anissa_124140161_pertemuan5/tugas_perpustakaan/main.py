# main.py
from library_item import Book, Magazine
from library import Library
from member import Member

if __name__ == "__main__":
    print("=== SISTEM MANAJEMEN PERPUSTAKAAN SEDERHANA ===\n")

    # 1. Inisialisasi Perpustakaan & Member
    perpus = Library()
    member1 = Member("M001", "Suci")
    print(f"Selamat datang, {member1.nama}!\n")

    # 2. Menambahkan Item (Buku & Majalah)
    buku1 = Book("B01", "Laskar Pelangi", "Andrea Hirata")
    buku2 = Book("B02", "Bumi Manusia", "Pramoedya Ananta Toer")
    majalah1 = Magazine("M01", "Bobo", "Edisi Januari 2024")

    perpus.tambah_item(buku1)
    perpus.tambah_item(buku2)
    perpus.tambah_item(majalah1)

    # 3. Menampilkan Katalog
    perpus.tampilkan_katalog()

    # 4. Mencari Item
    perpus.cari_item("bumi")     # Cari berdasarkan judul
    perpus.cari_item("M01")      # Cari berdasarkan ID

    # 5. Demonstrasi Peminjaman & Pengembalian (Encapsulation & Denda)
    print("\n--- SIMULASI PEMINJAMAN ---")
    perpus.pinjam_item("B01")
    perpus.pinjam_item("B01") # Coba pinjam lagi (harusnya gagal)
    
    print("\n--- SIMULASI PENGEMBALIAN ---")
    # Kembalikan dengan terlambat 3 hari
    perpus.kembalikan_item("B01", hari_terlambat=3)
    
    print("\n--- KATALOG TERAKHIR ---")
    perpus.tampilkan_katalog()