class Personaje:

    nombre = "Default"
    fuerza = 0
    vida = 0
    defensa = 0
    inteligencia = 0

    def __init__(self):
        pass

    def __str__(self):
        return "Soy un personaje"

mi_personaje = Personaje()
print(mi_personaje)