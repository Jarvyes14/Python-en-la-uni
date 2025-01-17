import os

class Personaje:

    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, vida, defensa, inteligencia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida
        self.defensa = defensa
        self.inteligencia = inteligencia
        # Self: Referencia al mismo  objeto
        # Init: Constructor que inicializa el atributo del objeto
        # Porque empieza con doble guion?: Porque es un método mágico
        # Cuando se ejecuta el método init?: Cuando se crea un objeto de la clase

    @property
    def imprimir_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Vida: {self.vida}")
        print(f"Defensa: {self.defensa}")
        print(f"Inteligencia: {self.inteligencia}")

    def subir_nivel(self,fuerza,vida,defensa,inteligencia):
        self.fuerza += fuerza
        self.vida += vida
        self.defensa += defensa
        self.inteligencia += inteligencia

    def morir(self):
        self.vida = 0
        print("El personaje ha muerto")

    def dañar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        enemigo.vida -= daño
        #Arreglado
        if enemigo.vida <= 0:
            enemigo.morir()
        return f"El enemigo ha recibido {daño} puntos de daño"

    def __str__(self):
        return "Soy un personaje"
    
class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, vida, defensa, inteligencia, espada):
        super().__init__(nombre, fuerza, vida, defensa, inteligencia)
        self.espada = espada

    def imprimir_atributos(self):
        super().imprimir_atributos
        print(f"Espada: {self.espada}")

    def elegir_arma(self):
        opcion = input("Elige un arma: \n(1)Lanza, daño 10 \n(2)Espada, daño 15 \n(3)Arco, daño 20 \n>")
        if opcion == "1":
            self.espada = 10
        elif opcion == "2":
            self.espada = 15
        elif opcion == "3":
            self.espada = 20
        else:
            print("Opción no válida \n")
            input("Presiona enter para continuar \n")
            os.system('cls')
            self.elegir_arma()
    
    def daño(self, enemigo):
        daño = self.fuerza * self.espada - enemigo.defensa
        enemigo.vida -= daño
        if enemigo.vida <= 0:
            enemigo.morir()
        return f"El enemigo ha recibido {daño} puntos de daño"
    
class Mago(Personaje):

    def __init__(self, nombre, fuerza, vida, defensa, inteligencia, libro):
        super().__init__(nombre, fuerza, vida, defensa, inteligencia)
        self.libro = libro

    def imprimir_atributos(self):
        super().imprimir_atributos
        print(f"Espada: {self.libro}")

    def elegir_arma(self):
        opcion = input("Elige un arma: \n(1)Libro de hechizos, daño 10 \n(2)Baculo, daño 15 \n(3)Varita, daño 20 \n>")
        if opcion == "1":
            self.libro = 10
        elif opcion == "2":
            self.libro = 15
        elif opcion == "3":
            self.libro = 20
        else:
            print("Opción no válida \n")
            input("Presiona enter para continuar \n")
            os.system('cls')
            self.elegir_arma()
    
    def daño(self, enemigo):
        daño = self.inteligencia * self.libro - enemigo.defensa
        enemigo.vida -= daño
        if enemigo.vida <= 0:
            enemigo.morir()
        return f"El enemigo ha recibido {daño} puntos de daño"


tlatoani = Guerrero("Tlatoani", 10, 100, 5, 20, 5)
tlatoani.elegir_arma()
tlatoani.imprimir_atributos()

mi_personaje = Personaje("Gandalf", 10, 100, 5, 20)
mi_personaje.imprimir_atributos
print("-----------------------")
tu_personaje = Personaje("Legolas", 15, 100, 10, 10)
tu_personaje.imprimir_atributos
print("-----------------------")
print(tu_personaje.dañar(mi_personaje))
print("-----------------------")
mi_personaje.imprimir_atributos
print("-----------------------")
tu_personaje.imprimir_atributos