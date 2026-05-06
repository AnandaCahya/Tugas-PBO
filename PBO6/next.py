
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

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
mahasiswa = []
for i in range(jumlah_mahasiswa):
    nim = input(f"Masukkan NIM mahasiswa: ")
    nama = input(f"Masukkan nama mahasiswa: ")
    mhs = Mhs(nim, nama, 0)
    nilai = int(input(f"Masukkan nilai mahasiswa: "))
    mhs.nilai = nilai
    mahasiswa.append(mhs)

print("\n============= Data Mahasiswa ===========")
print("NIM\tNama\tNilai\tGrade\tStatus Kelulusan")
for mhs in mahasiswa:
    if mhs.nilai >= 80:
        mhs._grade = 'A'
    elif mhs.nilai >= 65:
        mhs._grade = 'B'
    elif mhs.nilai >= 55:
        mhs._grade = 'C'
    elif mhs.nilai >= 50:
        mhs._grade = 'D'
    else:
        mhs._grade = 'E'
    print(f"{mhs.nim}\t{mhs.nama}\t{mhs.nilai}\t{mhs._grade}\t{Mhs.cek_kelulusan(mhs.nilai)}")