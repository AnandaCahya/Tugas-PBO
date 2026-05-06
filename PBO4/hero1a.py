class Hero:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
    
    # Method tanpa return, tanpa argumen
    def siapa(self):
        print("Nama hero adalah :", self.name)
    
    # Method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

suparman = Hero("Suparman", 100, 290, 100)
wonderwoman = Hero("Wonder Woman", 100, 170, 100)

suparman.siapa()
suparman.healthUp(20)
print("Health si suparman adalah", suparman.getHealth())