class Mhs:
    def __init__(self, nim, nama):
        self._nama = nama
        self._nim = nim
    
    @property
    def nim(self):
        return self._nim

    @property
    def nama(self):
        return self._nama
    
    @nim.setter
    def nim(self, nim):
        self._nim = nim

    @nama.setter
    def nama(self, nama):
        self._nama = nama
    
class Mhs_S1(Mhs):
    def __init__(self, nim, nama):
        super().__init__(nim, nama)
        self.jenjang = "Sarjana"
        self.max_semester = 14
    
class Mhs_S2(Mhs):
    def __init__(self, nim, nama):
        super().__init__(nim, nama)
        self.jenjang = "Pascasarjana"
        self.max_semester = 8

mhs_asia1 = Mhs_S1("2001", "Budi")
mhs_asia2 = Mhs_S2("2002", "Wati")

print(f"Nama: {mhs_asia1.nama}, NIM: {mhs_asia1.nim}, Jenjang: {mhs_asia1.jenjang}, Max Semester: {mhs_asia1.max_semester}")
print(f"Nama: {mhs_asia2.nama}, NIM: {mhs_asia2.nim}, Jenjang: {mhs_asia2.jenjang}, Max Semester: {mhs_asia2.max_semester}")

mhs_asia1.nim = "2003"
mhs_asia1.nama = "Selviana"

print(f"Nama: {mhs_asia1.nama}, NIM: {mhs_asia1.nim}, Jenjang: {mhs_asia1.jenjang}, Max Semester: {mhs_asia1.max_semester}")