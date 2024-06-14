# perpustakaan.py

from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun
        self.tersedia = True

    @abstractmethod
    def tampilkan_detail(self):
        pass

    def cek_ketersediaan(self):
        return self.tersedia

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            print(f"{self.judul} telah dipinjam.")
        else:
            print(f"{self.judul} tidak tersedia untuk dipinjam.")

    def kembalikan(self):
        if not self.tersedia:
            self.tersedia = True
            print(f"{self.judul} telah dikembalikan.")
        else:
            print(f"{self.judul} sudah tersedia.")

class Buku(ItemPerpustakaan):
    def __init__(self, judul, penulis, tahun):
        super().__init__(judul, tahun)
        self.penulis = penulis

    def tampilkan_detail(self):
        print(f"Buku: {self.judul} oleh {self.penulis}, Tahun: {self.tahun}")

class Majalah(ItemPerpustakaan):
    def __init__(self, judul, edisi, penerbit):
        super().__init__(judul, None)
        self.edisi = edisi
        self.penerbit = penerbit

    def tampilkan_detail(self):
        print(f"Majalah: {self.judul}, Edisi: {self.edisi}, Penerbit: {self.penerbit}")

class Perpustakaan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.katalog = []

    def tambah_item(self, item):
        self.katalog.append(item)

    def tampilkan_katalog(self):
        print(f"Katalog {self.nama}:")
        for item in self.katalog:
            item.tampilkan_detail()

    def cari_item(self, judul):
        for item in self.katalog:
            if item.judul == judul:
                return item
        return None
