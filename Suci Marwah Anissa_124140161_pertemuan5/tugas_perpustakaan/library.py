# library.py
class Library:
    def __init__(self):
        # Encapsulation: Private attribute (tidak bisa diakses langsung dari luar)
        self.__koleksi = []

    def tambah_item(self, item):
        self.__koleksi.append(item)
        print(f"[+] Berhasil menambahkan: '{item.judul}' ke perpustakaan.")

    def tampilkan_katalog(self):
        print("\n=== KATALOG PERPUSTAKAAN ===")
        if len(self.__koleksi) == 0:
            print("Perpustakaan masih kosong.")
            return
            
        for item in self.__koleksi:
            # Polymorphism: memanggil get_detail() tanpa peduli itu Book atau Magazine
            print(item.get_detail())

    def cari_item(self, keyword: str):
        print(f"\n=== PENCARIAN: '{keyword}' ===")
        ditemukan = False
        for item in self.__koleksi:
            # Cari berdasarkan ID atau Judul (menggunakan lower() agar tidak case-sensitive)
            if keyword.lower() in item.judul.lower() or keyword == item.id_item:
                print(item.get_detail())
                ditemukan = True
        
        if not ditemukan:
            print("Maaf, item tidak ditemukan.")

    def pinjam_item(self, id_item: str):
        for item in self.__koleksi:
            if item.id_item == id_item:
                if not item.is_dipinjam:
                    item.is_dipinjam = True
                    print(f"[-] Item '{item.judul}' berhasil dipinjam.")
                else:
                    print(f"[!] Item '{item.judul}' sedang dipinjam orang lain.")
                return
        print(f"[!] Item dengan ID {id_item} tidak ada.")

    def kembalikan_item(self, id_item: str, hari_terlambat: int = 0):
        for item in self.__koleksi:
            if item.id_item == id_item:
                if item.is_dipinjam:
                    item.is_dipinjam = False
                    denda = item.hitung_denda(hari_terlambat)
                    print(f"[-] Item '{item.judul}' telah dikembalikan.")
                    if denda > 0:
                        print(f"    Total Denda (Telat {hari_terlambat} hari): Rp {denda:,.0f}")
                else:
                    print(f"[!] Item '{item.judul}' tidak sedang dipinjam.")
                return
        print(f"[!] Item dengan ID {id_item} tidak ada.")