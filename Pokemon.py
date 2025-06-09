class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
    
    debilidades = {
        "Fuego" : "Agua",
        "Agua" : "Planta",
        "Agua" : "Electrico",
        "Planta" : "Fuego"
    }
    
    def info(self):
        print(f"{self.nombre} - {self.vida} PS - LVL {self.nivel}")

    def debil(self):
        self.defensa = self.defensa*0.8

    def debilidad(self, enemigo):
        if Pokemon.debilidades.get(self.tipo) == enemigo.tipo:
                self.debil()

pikachu = Pokemon("Pikachu", "Electrico", 5, 20, 10, 10)
charmander = Pokemon("Charmander", "Fuego", 5, 19, 12, 8)
bulbasaur = Pokemon("Bulbasaur", "Planta", 5, 20, 9, 10)
squirtle = Pokemon("Squirtle", "Agua", 5, 20, 10, 10)