print("Bienvenido a la batalla Pokemon!")

# P1 = Pikachu

P1Nombre = "Pikachu"
P1HP = 40
P1ATK = 10
P1DEF = 10
P1SPD = 10
P1ACU = 90

# P2 = Fomantis

P2Nombre = "Fomantis"
P2HP = 40
P2ATK = 8
P2DEF = 12
P2SPD = 12
P2ACU = 80

print("Elige a tu Pokemon, escribe el numero para seleccionar: ")
pokejugador = int(input("1." + P1Nombre + " 2." + P2Nombre + ": "))

if pokejugador == 1:
    pokeenemigo = 2
elif pokejugador == 2:
    pokeenemigo = 1

def batalla