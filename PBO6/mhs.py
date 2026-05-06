class Mhs:
    # Atribut kelas
    institusi = "Universitas Teknologi dan Bisnis Asia"
    jumlah_mhs = 0

    def __init__(self, nim, nama, nilai):
        self._nama = nama
        self._nim = nim
        self._nilai = nilai
        Mhs.jumlah_mhs += 1

    # Property
    @property
    def nama(self):
        return self._nama
    @property
    def nim(self):
        return self._nim
    @property
    def nilai(self):
        return self._nilai

    # Property Setter
    @nama.setter
    def nama(self, nama):
        self._nama = nama
    @nim.setter
    def nim(self, nim):
        self._nim = nim
    @nilai.setter
    def nilai(self, skor):
        if 0 <= skor <= 100:
            self._nilai = skor
        else:
            print("Kesalahan: Nilai harus diantara 0 - 100!")
    
    # Property Deleter
    @nilai.deleter
    def nilai(self):
        print(f"Menghapus data nilai untuk {self.nama}...")
        self._nilai = 0

    # Static Method
    @staticmethod
    def cek_kelulusan(skor):
        return "LULUS" if skor >= 60 else "TIDAK LULUS"
    
    # Class Method
    @classmethod
    def ubah_institusi(cls, nama_baru):
        cls.institusi = nama_baru
        print(f"Nama institusi berhasil diubah menjadi {cls.institusi}")

mhs1 = Mhs("230001", "Budi", 0)
# Merubah nilai mhs1
mhs1.nilai = 85
# Menampilkan nama dan nilai mhs1
print(f"{mhs1.nama} dengan NIM {mhs1.nim} nilainya {mhs1.nilai}")
# Mengecek nilai mahasiswa lulus atau tidak
status = Mhs.cek_kelulusan(mhs1.nilai)
print(f"Status kelulusan: {status}")
# Perubahan nama institusi
Mhs.ubah_institusi("Institut Asia Malang")
# Menghapus nilai mhs1
del mhs1.nilai
print(f"Nilai setelah dihapus: {mhs1.nilai}")

mhs2 = Mhs("230002", "Wati", 0)
# Merubah nilai mhs2
mhs2.nilai = 55
# Menampilkan nama dan nilai mhs2
print(f"Mahasiswa {mhs2.nama} nilainya {mhs2.nilai}")
# Mengecek nilai mahasiswa lulus atau tidak
status = Mhs.cek_kelulusan(mhs2.nilai)
print(f"Status kelulusan: {status}")
print(f"Institut mahasiswa: {mhs2.nama} adalah di {mhs2.institusi}")