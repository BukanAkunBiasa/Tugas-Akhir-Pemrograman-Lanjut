# pustakawan.py

from perpustakaan import ItemPerpustakaan, Perpustakaan

class Pustakawan:
    def __init__(self, nama, perpustakaan):
        self.nama = nama
        self.perpustakaan = perpustakaan

    def tampilkan_item_tersedia(self):
        print(f"Item yang tersedia di {self.perpustakaan.nama}:")
        for item in self.perpustakaan.katalog:
            if item.cek_ketersediaan():
                item.tampilkan_detail()

    def pinjam_item(self, judul):
        item = self.perpustakaan.cari_item(judul)
        if item:
            item.pinjam()
        else:
            print(f"{judul} tidak ditemukan di perpustakaan.")

    def kembalikan_item(self, judul):
        item = self.perpustakaan.cari_item(judul)
        if item:
            item.kembalikan()
        else:
            print(f"{judul} tidak ditemukan di perpustakaan.")
