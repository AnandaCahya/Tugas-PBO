class pahlawan():
    def __init__(self, nama, health, power, armor, posisi = 0):
        self.nama = nama
        self.health = health
        self.power = power
        self.armor = armor
        self.posisi = posisi
    
    def jalan(self, jarak):
        self.posisi += 5


gatotkaca = pahlawan("Gatotkaca", 100, 10, 100)
cutnyadien = pahlawan("Cut Nyak Dien", 100, 10, 100)
kartini = pahlawan("R.A Kartini", 100, 10, 100)
soedirman = pahlawan("Jendral Soedirman", 100, 10, 100)
hatta = pahlawan("Drs. Mohammad Hatta", 100, 10, 100)
jarak = 5
print("Nama pahlawan ini adalah", gatotkaca.nama, "berjalan sejauh", jarak, "km", "diposisi awal", gatotkaca.posisi)
gatotkaca.jalan(jarak)
print("Sekarang berada di", gatotkaca.posisi)
print("Bertemu dengan", cutnyadien.nama, "dan", kartini.nama)

# Jalan Lagi
print("Berjalan lagi sejauh", jarak, "km", "diposisi awal", gatotkaca.posisi)
gatotkaca.jalan(12)
print("Sekarang dia berada di", gatotkaca.posisi)
print("Bertemu dengan", soedirman.nama, "dan", hatta.nama)