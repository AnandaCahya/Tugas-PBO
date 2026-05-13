from datetime import datetime
import random


class Buku:
    def __init__(self, kode, judul, penulis, tahun_terbit):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.tersedia = True


class Anggota:
    def __init__(self, nomor, nama, alamat, telp):
        self.nomor = nomor
        self.nama = nama
        self.alamat = alamat
        self.telp = telp


class Peminjaman:
    def __init__(self, no_transaksi, anggota, buku):
        self.no_transaksi = no_transaksi
        self.anggota = anggota
        self.buku = buku
        self.tgl_pinjam = datetime.now()
        self.tgl_kembali = None
        self.status = "Dipinjam"


class SiPerpus:
    def __init__(self):
        self.buku = []
        self.anggota = []
        self.riwayat = []

    def cari_anggota_nomor(self, nomor):
        arr = self.anggota.copy()

        for i in range(len(arr)):
            if arr[i].nomor == nomor:
                return i

        return -1

    def cari_buku_kode(self, kode):
        arr = self.buku.copy()

        for i in range(len(arr)):
            if arr[i].kode == kode:
                return i

        return -1

    def cari_transaksi_buku(self, kode):
        arr = self.riwayat.copy()

        for i in range(len(arr)):
            if arr[i].buku.kode == kode and arr[i].status == "Dipinjam":
                return i

        return -1

    def buat_nomor_anggota(self):
        nomor = str(random.randint(1, 999999)).zfill(6)

        ada = self.cari_anggota_nomor(nomor)

        if ada != -1:
            return self.buat_nomor_anggota()

        return nomor

    def buat_nomor_transaksi(self):
        return "TRX" + str(random.randint(1000, 9999))

    def tambah_buku(self, kode, judul, penulis, tahun_terbit):
        ada = self.cari_buku_kode(kode)

        if ada != -1:
            return -1

        buku = Buku(kode, judul, penulis, tahun_terbit)
        self.buku.append(buku)

        return buku

    def tambah_anggota(self, nama, alamat, telp):
        nomor = self.buat_nomor_anggota()

        anggota = Anggota(nomor, nama, alamat, telp)

        self.anggota.append(anggota)

        return anggota

    def pinjam_buku(self, nomoranggota, kodebuku):
        idx_anggota = self.cari_anggota_nomor(nomoranggota)

        if idx_anggota == -1:
            return -1

        idx_buku = self.cari_buku_kode(kodebuku)

        if idx_buku == -1:
            return -2

        anggota = self.anggota[idx_anggota]
        buku = self.buku[idx_buku]

        if not buku.tersedia:
            return -3

        buku.tersedia = False

        transaksi = Peminjaman(
            self.buat_nomor_transaksi(),
            anggota,
            buku
        )

        self.riwayat.append(transaksi)

        return transaksi

    def kembalikan_buku(self, kodebuku):
        idx_buku = self.cari_buku_kode(kodebuku)

        if idx_buku == -1:
            return -1

        buku = self.buku[idx_buku]

        if buku.tersedia:
            return -2

        idx_transaksi = self.cari_transaksi_buku(kodebuku)

        transaksi = self.riwayat[idx_transaksi]

        transaksi.status = "Dikembalikan"
        transaksi.tgl_kembali = datetime.now()

        buku.tersedia = True

        return transaksi

    def info_anggota(self, nomor):
        idx = self.cari_anggota_nomor(nomor)

        if idx == -1:
            return -1

        anggota = self.anggota[idx]

        daftar_pinjam = []

        for trx in self.riwayat:
            if trx.anggota.nomor == nomor and trx.status == "Dipinjam":
                daftar_pinjam.append(trx)

        return anggota, daftar_pinjam

    def daftar_buku(self):
        return self.buku

    def riwayat_peminjaman(self):
        return self.riwayat


"""
Sistem Perpustakaan
"""

perpus = SiPerpus()


"""
UI PROGRAM
"""


def TambahBuku():
    print("\n=== TAMBAH DATA BUKU ===")

    while True:
        kode = input("Masukkan kode buku : ")

        cek = perpus.cari_buku_kode(kode)

        if cek != -1:
            print("Kode buku sudah ada!")
        else:
            break

    judul = input("Masukkan judul buku : ")
    penulis = input("Masukkan penulis : ")
    tahun = input("Masukkan tahun terbit : ")

    buku = perpus.tambah_buku(
        kode,
        judul,
        penulis,
        tahun
    )

    print("Data buku berhasil ditambahkan!")
    print(f"Kode Buku : {buku.kode}")


def TambahAnggota():
    print("\n=== TAMBAH DATA ANGGOTA ===")

    nama = input("Masukkan nama : ")
    alamat = input("Masukkan alamat : ")
    hp = input("Masukkan nomor HP : ")

    anggota = perpus.tambah_anggota(
        nama,
        alamat,
        hp
    )

    print("\nData anggota berhasil ditambahkan!")
    print(f"Nomor Anggota : {anggota.nomor}")


def PinjamBuku():
    print("\n=== PINJAM BUKU ===")

    nomor = input("Masukkan nomor anggota : ")

    idx = perpus.cari_anggota_nomor(nomor)

    if idx == -1:
        print("Anggota tidak ditemukan!")
        return

    anggota = perpus.anggota[idx]

    print("\nData Anggota")
    print(f"Nama    : {anggota.nama}")
    print(f"Alamat  : {anggota.alamat}")
    print(f"No HP   : {anggota.telp}")

    while True:
        kode = input("\nMasukkan kode buku : ")

        hasil = perpus.pinjam_buku(
            nomor,
            kode
        )

        if hasil == -2:
            print("Kode buku tidak tersedia!")
            continue

        if hasil == -3:
            print("Buku sedang dipinjam!")
            return

        transaksi = hasil

        print("\n=== DATA PEMINJAMAN ===")
        print(f"No Transaksi : {transaksi.no_transaksi}")
        print(f"Nama Anggota : {transaksi.anggota.nama}")
        print(f"Judul Buku   : {transaksi.buku.judul}")
        print(f"Tanggal      : {transaksi.tgl_pinjam}")

        break


def KembalikanBuku():
    print("\n=== KEMBALIKAN BUKU ===")

    while True:
        kode = input("Masukkan kode buku : ")

        hasil = perpus.kembalikan_buku(kode)

        if hasil == -1:
            print("Kode buku tidak tersedia!")
            continue

        if hasil == -2:
            print("Buku ini tidak sedang dipinjam!")
            return

        transaksi = hasil

        print("\n=== DATA PENGEMBALIAN ===")
        print(f"No Transaksi : {transaksi.no_transaksi}")
        print(f"Nama Anggota : {transaksi.anggota.nama}")
        print(f"Judul Buku   : {transaksi.buku.judul}")
        print(f"Tanggal      : {transaksi.tgl_kembali}")

        break


def InfoAnggota():
    print("\n=== INFO ANGGOTA ===")

    while True:
        nomor = input("Masukkan nomor anggota : ")

        hasil = perpus.info_anggota(nomor)

        if hasil == -1:
            print("Anggota tidak ditemukan!")
        else:
            break

    anggota, daftar = hasil

    print("\n=== DATA ANGGOTA ===")
    print(f"Nomor Anggota : {anggota.nomor}")
    print(f"Nama          : {anggota.nama}")
    print(f"Alamat        : {anggota.alamat}")
    print(f"Nomor HP      : {anggota.telp}")

    print("\n=== DAFTAR PINJAMAN ===")

    if len(daftar) == 0:
        print("Tidak ada buku yang dipinjam")
        return

    print("No\tKode\tJudul\t\tStatus")

    no = 1

    for trx in daftar:
        print(
            f"{no}\t"
            f"{trx.buku.kode}\t"
            f"{trx.buku.judul}\t\t"
            f"{trx.status}"
        )

        no += 1


def DaftarBuku():
    print("\n=== DAFTAR BUKU ===")

    daftar = perpus.daftar_buku()

    if len(daftar) == 0:
        print("Belum ada data buku")
        return

    print("No\tKode\tJudul\tPenulis\tTahun\tStatus")

    no = 1

    for buku in daftar:
        status = "Tersedia"

        if not buku.tersedia:
            status = "Dipinjam"

        print(
            f"{no}\t"
            f"{buku.kode}\t"
            f"{buku.judul}\t"
            f"{buku.penulis}\t"
            f"{buku.tahun_terbit}\t"
            f"{status}"
        )

        no += 1


def RiwayatPeminjaman():
    print("\n=== RIWAYAT PEMINJAMAN ===")

    daftar = perpus.riwayat_peminjaman()

    if len(daftar) == 0:
        print("Belum ada riwayat peminjaman")
        return

    print(
        "No\tNo Transaksi\tTgl Pinjam\t\t"
        "Tgl Kembali\t\tNama\tKode\tJudul\tStatus"
    )

    no = 1

    for trx in daftar:
        kembali = "-"

        if trx.tgl_kembali:
            kembali = trx.tgl_kembali.strftime("%d-%m-%Y %H:%M")

        print(
            f"{no}\t"
            f"{trx.no_transaksi}\t"
            f"{trx.tgl_pinjam.strftime('%d-%m-%Y %H:%M')}\t"
            f"{kembali}\t"
            f"{trx.anggota.nama}\t"
            f"{trx.buku.kode}\t"
            f"{trx.buku.judul}\t"
            f"{trx.status}"
        )

        no += 1


# MAIN PROGRAM
while True:
    print("\n")
    print("\t\t=== SISTEM PERPUSTAKAAN ===")

    print("""
1. Tambah Data Buku
2. Tambah Data Anggota
3. Pinjam Buku
4. Kembalikan Buku
5. Info Anggota
6. Daftar Buku
7. Riwayat Peminjaman
8. Keluar
    """)

    try:
        opsi = int(input("Pilih menu : "))

        match opsi:
            case 1:
                TambahBuku()

            case 2:
                TambahAnggota()

            case 3:
                PinjamBuku()

            case 4:
                KembalikanBuku()

            case 5:
                InfoAnggota()

            case 6:
                DaftarBuku()

            case 7:
                RiwayatPeminjaman()

            case 8:
                print("Program selesai")
                break

            case _:
                print("Menu tidak tersedia!")

    except:
        print("Input harus angka!")