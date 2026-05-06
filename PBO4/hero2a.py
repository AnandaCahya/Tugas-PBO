class Hero:
    jumlah_hero = 0

    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_hero += 1

        self.__age = 70 # Instance variable: private
        self._weight = 110 # Instance variable: protected
    
suparman = Hero("Suparman", 100, 170, 100)
print("=========== Memanggil var jumlah ===========")
print("Punya object :", suparman.jumlah_hero)
print("Punya class :", Hero.jumlah_hero)
print("==== Nilai jumlah hero di object dirubah ===")
suparman.jumlah_hero = 10
print("Punya object :", suparman.jumlah_hero)
print("Punya class :", Hero.jumlah_hero)
print("==== Nilai jumlah hero di class dirubah ====")
Hero.jumlah_hero = 20
print("Punya object :", suparman.jumlah_hero)
print("Punya class :", Hero.jumlah_hero)

# Private & protected
print(suparman.__dict__)
# print("Umur suparman", suparman.__age)
suparman.__age = 17
print(suparman.__dict__)
print("Umur suparman", suparman.__age)
suparman._weight = 80
print(suparman.__dict__)
