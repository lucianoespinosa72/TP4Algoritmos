from lista import Lista
from personaje import Personaje


def cargar_personajes():
    """Crea la lista de personajes ordenada por nombre."""
    datos = [
        ("Luke Skywalker", 172, 53, "Masculino", "Humano", "Tatooine", [4, 5, 6, 7, 8, 9]),
        ("Leia Organa", 150, 53, "Femenino", "Humano", "Alderaan", [4, 5, 6, 7, 8, 9]),
        ("Han Solo", 180, 66, "Masculino", "Humano", "Corellia", [4, 5, 6, 7]),
        ("Darth Vader", 202, 45, "Masculino", "Humano", "Tatooine", [3, 4, 5, 6]),
        ("Chewbacca", 228, 234, "Masculino", "Wookiee", "Kashyyyk", [3, 4, 5, 6, 7, 8, 9]),
        ("C-3PO", 167, 66, "Ninguno", "Droide", "Tatooine", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ("R2-D2", 96, 66, "Ninguno", "Droide", "Naboo", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ("BB-8", 67, 5, "Ninguno", "Droide", "Desconocido", [7, 8, 9]),
        ("Yoda", 66, 900, "Masculino", "Desconocida", "Desconocido", [1, 2, 3, 5, 6]),
        ("Maz Kanata", 124, 1000, "Femenino", "Desconocida", "Takodana", [7, 8, 9]),
        ("Padmé Amidala", 165, 27, "Femenino", "Humano", "Naboo", [1, 2, 3]),
        ("Rey", 170, 23, "Femenino", "Humano", "Jakku", [7, 8, 9]),
        ("Mon Mothma", 150, 48, "Femenino", "Humano", "Chandrila", [6]),
        ("Wedge Antilles", 170, 40, "Masculino", "Humano", "Corellia", [4, 5, 6]),
        ("Bail Organa", 191, 67, "Masculino", "Humano", "Alderaan", [2, 3]),
        ("Jabba el Hutt", 175, 600, "Masculino", "Hutt", "Nal Hutta", [1, 4, 6]),
        ("Wicket", 88, 8, "Masculino", "Ewok", "Endor", [6]),
        ("Lando Calrissian", 177, 53, "Masculino", "Humano", "Socorro", [5, 6, 9]),
    ]

    lista = Lista(criterio=lambda personaje: personaje.nombre)
    for nombre, altura, edad, genero, especie, planeta, episodios in datos:
        lista.insertar(Personaje(nombre, altura, edad, genero, especie, planeta, episodios))
    return lista


# a. Personajes de un género dado
def personajes_por_genero(lista, genero):
    return [personaje.nombre for personaje in lista if personaje.genero == genero]


# b. Personajes de una especie que aparecieron en todos los episodios indicados
def especie_en_episodios(lista, especie, episodios):
    return [personaje.nombre for personaje in lista
            if personaje.especie == especie and set(episodios) <= set(personaje.episodios)]


# c. Toda la información de los personajes indicados
def informacion_de(lista, nombres):
    return [lista.buscar(nombre) for nombre in nombres]


# d. Personajes que aparecen en todos los episodios indicados
def personajes_en_episodios(lista, episodios):
    return [personaje.nombre for personaje in lista
            if set(episodios) <= set(personaje.episodios)]


# e. Personajes con edad mayor a un valor dado, y el mayor de ellos
def mayores_a(lista, edad):
    resultado = [personaje for personaje in lista if personaje.edad > edad]
    mayor = max(resultado, key=lambda personaje: personaje.edad) if resultado else None
    return resultado, mayor


# f. Eliminar los personajes que aparecieron solamente en los episodios indicados
def eliminar_solo_en_episodios(lista, episodios):
    a_eliminar = [personaje.nombre for personaje in lista
                  if set(personaje.episodios) == set(episodios)]
    for nombre in a_eliminar:
        lista.eliminar(nombre)
    return a_eliminar


# g. Personajes de una especie nacidos en un planeta dado
def especie_de_planeta(lista, especie, planeta):
    return [personaje.nombre for personaje in lista
            if personaje.especie == especie and personaje.planeta_natal == planeta]


# h. Personajes con altura menor a un valor dado (en cm)
def menores_en_altura(lista, altura):
    return [personaje for personaje in lista if personaje.altura < altura]


# i. Episodios en los que aparece un personaje, junto con su información
def episodios_de(lista, nombre):
    return lista.buscar(nombre)


def main():
    personajes = cargar_personajes()

    print("a. Personajes de género femenino:")
    for nombre in personajes_por_genero(personajes, "Femenino"):
        print(" -", nombre)

    print("\nb. Droides que aparecieron en los episodios I a VI:")
    for nombre in especie_en_episodios(personajes, "Droide", [1, 2, 3, 4, 5, 6]):
        print(" -", nombre)

    print("\nc. Información de Darth Vader y Han Solo:")
    for nombre, personaje in zip(["Darth Vader", "Han Solo"],
                                 informacion_de(personajes, ["Darth Vader", "Han Solo"])):
        print(" -", personaje if personaje else f"{nombre}: no encontrado")

    print("\nd. Personajes que aparecen en el episodio VII y en los tres anteriores (IV, V, VI):")
    for nombre in personajes_en_episodios(personajes, [4, 5, 6, 7]):
        print(" -", nombre)

    print("\ne. Personajes con más de 850 años:")
    viejos, mayor = mayores_a(personajes, 850)
    for personaje in viejos:
        print(f" - {personaje.nombre} ({personaje.edad} años)")
    if mayor:
        print(f"   El mayor es {mayor.nombre} con {mayor.edad} años")

    print("\nf. Eliminar personajes que aparecieron solamente en los episodios IV, V y VI:")
    eliminados = eliminar_solo_en_episodios(personajes, [4, 5, 6])
    for nombre in eliminados:
        print(" - Eliminado:", nombre)
    print("   Quedan", len(personajes), "personajes")

    print("\ng. Humanos cuyo planeta de origen es Alderaan:")
    for nombre in especie_de_planeta(personajes, "Humano", "Alderaan"):
        print(" -", nombre)

    print("\nh. Personajes con altura menor a 70 cm:")
    for personaje in menores_en_altura(personajes, 70):
        print(" -", personaje)

    print("\ni. Episodios en los que aparece Chewbacca:")
    chewbacca = episodios_de(personajes, "Chewbacca")
    if chewbacca:
        print("   Episodios:", chewbacca.episodios_romanos())
        print("   Información:", chewbacca)
    else:
        print("   Chewbacca no está en la lista")


if __name__ == "__main__":
    main()
