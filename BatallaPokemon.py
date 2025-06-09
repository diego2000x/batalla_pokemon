import Pokemon

print("Bienvenido a la batalla Pokemon!")

class Batalla:
    def __init__(self, aliado, enemigo):
        self.aliado = aliado
        self.enemigo = enemigo
    
    def saludo(self):
        print(f"El {self.enemigo.nombre} quiere pelear")
        print(f"Ve, {self.aliado.nombre}!")

    def status(self):
        self.aliado.info()
        self.enemigo.info()

    def comenzar(self):
        self.saludo()
        self.status()
       # self.duelo(self, enemigo)

duelo1 = Batalla(Pokemon.charmander, Pokemon.squirtle)
duelo1.comenzar()
