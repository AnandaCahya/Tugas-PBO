class mhs():
    pass

saya = mhs()
kawan1 = mhs()
kawan2 = mhs()

saya.nim = "202011127"
saya.nama = "Nanda"
saya.gender = "Laki Laki"
saya.prodi = "TI"

kawan1.nim = "202012188"
kawan1.nama = "Carla"
kawan1.gender = "Perempuan"
kawan1.prodi = "Manajemen"

kawan2.nim = "202021922"
kawan2.nama = "Reza"
kawan2.gender = "Laki Laki"
kawan2.prodi = "DKV"

print(saya)
print(saya.__dict__)
print("Nama teman saya", kawan1.nama, "dan teman saya", kawan2.nama)