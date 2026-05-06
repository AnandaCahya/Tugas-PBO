class mhs():
    def __init__(self, nama, nim, gender, prodi):
        self.nama = nama
        self.nim = nim
        self.gender = gender
        self.prodi = prodi

saya = mhs("Nanda", "202011127", "Laki Laki", "TI")
kawan1 = mhs("Clarissa", "202013189", "Perempuan", "DKV")
kawan2 = mhs("Annisa", "202012190", "Perempuan", "Manajemen")

print("Aku seorang", saya.gender, "bernama", saya.nama, "kuliah asia di jurusan", saya.prodi, "punya teman diprodi", kawan1.prodi, "namanya", kawan1.nama)
print("Aku juga punya", kawan2.gender, "di prodi", kawan2.prodi, "namanya", kawan2.nama)
print("NIM kami adalah", saya.nim + ",", kawan1.nim + ",", kawan2.nim)