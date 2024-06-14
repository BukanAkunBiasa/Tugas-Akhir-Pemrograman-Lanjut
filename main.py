# utama.py

from perpustakaan import Perpustakaan, Buku, Majalah
from pustakawan import Pustakawan

def main():
    # Buat instance perpustakaan
    perpustakaan = Perpustakaan("Perpustakaan Malang", "Jl. Supriyadi No. 123")

    # Tambah buku dan majalah ke perpustakaan
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2019)
    buku2 = Buku("Atomic Habits", "James Clear", 2020)
    majalah1 = Majalah("Swantara Kematangan Demokrasi", "14, Desember 2023", "Lemhannas RI")

    perpustakaan.tambah_item(buku1)
    perpustakaan.tambah_item(buku2)
    perpustakaan.tambah_item(majalah1)

    # Buat pustakawan untuk mengelola perpustakaan
    pustakawan = Pustakawan("Prabowo Aniess", perpustakaan)

    # Demonstrasi operasi perpustakaan
    pustakawan.tampilkan_item_tersedia()
    pustakawan.pinjam_item("Laskar Pelangi")
    pustakawan.pinjam_item("Atomic Habits")
    pustakawan.tampilkan_item_tersedia()
    pustakawan.kembalikan_item("Laskar Pelangi")
    pustakawan.tampilkan_item_tersedia()

if __name__ == "__main__":
    main()
