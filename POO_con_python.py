class Personaje:

    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, vida, defensa, inteligencia):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__vida = vida
        self.__defensa = defensa
        self.__inteligencia = inteligencia
        # Self: Referencia al mismo  objeto
        # Init: Constructor que inicializa el atributo del objeto
        # Porque empieza con doble guion?: Porque es un método mágico
        # Cuando se ejecuta el método init?: Cuando se crea un objeto de la clase

    @property
    def imprimir_atributos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Fuerza: {self.__fuerza}")
        print(f"Vida: {self.__vida}")
        print(f"Defensa: {self.__defensa}")
        print(f"Inteligencia: {self.__inteligencia}")

    def subir_nivel(self,fuerza,vida,defensa,inteligencia):
        self.__fuerza += fuerza
        self.__vida += vida
        self.__defensa += defensa
        self.__inteligencia += inteligencia

    def __morir(self):
        self.__vida = 0
        print("El personaje ha muerto")

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            raise ValueError("La fuerza no puede ser negativa")
        else:
            self.__fuerza = fuerza
        self.__fuerza = fuerza

    def get_fuerza(self):
        return self.__fuerza

    def dañar(self, enemigo):
        daño = self.__fuerza - enemigo.__defensa
        enemigo.__vida -= daño
        if enemigo.__vida <= 0:
            enemigo.__morir()
        return f"El enemigo ha recibido {daño} puntos de daño"

    def __str__(self):
        return "Soy un personaje"

mi_personaje = Personaje("Gandalf", 100, 100, 5, 20)
#mi_personaje.imprimir_atributos
#print("-----------------------")
tu_personaje = Personaje("Legolas", 150, 100, 10, 10)
#tu_personaje.imprimir_atributos
#print("-----------------------")
#print(tu_personaje.dañar(mi_personaje))
#print("-----------------------")
#mi_personaje.imprimir_atributos
#print("-----------------------")
#tu_personaje.imprimir_atributos
#print("-----------------------")
try:
    mi_personaje.__morir()
except:
    print("No se puede acceder al método privado __morir")

mi_personaje.set_fuerza(200)
print(mi_personaje.get_fuerza())