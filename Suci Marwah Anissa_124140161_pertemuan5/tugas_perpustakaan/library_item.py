# library_item.py
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """Abstract class untuk semua item perpustakaan"""
    def __init__(self, id_item: str, judul: str):
        self.id_item = id_item
        self.judul = judul
        self._is_dipinjam = False  # Protected attribute

    # Menerapkan @property (Encapsulation)
    @property
    def is_dipinjam(self) -> bool:
        return self._is_dipinjam

    @is_dipinjam.setter
    def is_dipinjam(self, status: bool):
        self._is_dipinjam = status

    # Abstract methods yang wajib dioverride
    @abstractmethod
    def get_detail(self) -> str:
        pass

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        pass


class Book(LibraryItem):
    def __init__(self, id_item: str, judul: str, penulis: str):
        super().__init__(id_item, judul)
        self.penulis = penulis

    # Implementasi abstract method
    def get_detail(self) -> str:
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return f"[Buku] ID: {self.id_item} | {self.judul} | Penulis: {self.penulis} | Status: {status}"

    def hitung_denda(self, hari_terlambat: int) -> float:
        # Denda buku Rp 2.000 per hari
        return hari_terlambat * 2000


class Magazine(LibraryItem):
    def __init__(self, id_item: str, judul: str, edisi: str):
        super().__init__(id_item, judul)
        self.edisi = edisi

    def get_detail(self) -> str:
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return f"[Majalah] ID: {self.id_item} | {self.judul} | Edisi: {self.edisi} | Status: {status}"

    def hitung_denda(self, hari_terlambat: int) -> float:
        # Denda majalah lebih murah, Rp 1.000 per hari
        return hari_terlambat * 1000