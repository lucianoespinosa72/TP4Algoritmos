from lista import Lista
from superheroe import Superheroe


def cargar_superheroes():
    """Crea la lista de superhéroes ordenada por nombre."""
    datos = [
        ("Linterna Verde", 1940, "DC", "Hal Jordan usa un anillo de poder que crea construcciones de energía verde."),
        ("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y un factor de curación acelerado."),
        ("Dr. Strange", 1963, "DC", "Hechicero Supremo, protector de la Tierra ante amenazas místicas."),
        ("Iron Man", 1963, "Marvel", "Tony Stark, genio millonario que combate el crimen con una armadura de alta tecnología."),
        ("Capitana Marvel", 1968, "Marvel", "Carol Danvers, piloto que obtuvo poderes cósmicos tras fusionarse con energía Kree."),
        ("Mujer Maravilla", 1941, "DC", "Diana, princesa amazona de Themyscira con el lazo de la verdad."),
        ("Flash", 1940, "DC", "Barry Allen, el hombre más rápido del mundo, conectado a la Fuerza de la Velocidad."),
        ("Star-Lord", 1976, "Marvel", "Peter Quill, líder de los Guardianes de la Galaxia."),
        ("Batman", 1939, "DC", "Bruce Wayne usa un traje de murciélago y su intelecto para proteger Gotham."),
        ("Superman", 1938, "DC", "Kal-El, último hijo de Krypton, viste un traje azul con capa roja."),
        ("Spider-Man", 1962, "Marvel", "Peter Parker, adolescente con poderes arácnidos y un traje rojo y azul."),
        ("Black Panther", 1966, "Marvel", "T'Challa, rey de Wakanda, usa un traje de vibranium."),
        ("Hulk", 1962, "Marvel", "Bruce Banner se transforma en un gigante verde cuando se enoja."),
        ("Aquaman", 1941, "DC", "Arthur Curry, rey de la Atlántida, se comunica con la vida marina."),
        ("Capitán América", 1941, "Marvel", "Steve Rogers, supersoldado armado con un escudo de vibranium."),
        ("Mera", 1963, "DC", "Reina de la Atlántida con el poder de controlar el agua."),
    ]

    lista = Lista(criterio=lambda heroe: heroe.nombre)
    for nombre, anio, casa, biografia in datos:
        lista.insertar(Superheroe(nombre, anio, casa, biografia))
    return lista


# a. Eliminar un superhéroe por nombre
def eliminar_superheroe(lista, nombre):
    return lista.eliminar(nombre)


# b. Año de aparición de un superhéroe
def anio_de_aparicion(lista, nombre):
    heroe = lista.buscar(nombre)
    return heroe.anio_aparicion if heroe is not None else None


# c. Cambiar la casa de un superhéroe
def cambiar_casa(lista, nombre, nueva_casa):
    heroe = lista.buscar(nombre)
    if heroe is not None:
        heroe.casa = nueva_casa
        return True
    return False


# d. Superhéroes cuya biografía menciona alguna de las palabras
def heroes_con_palabras_en_biografia(lista, palabras):
    resultado = []
    for heroe in lista:
        biografia = heroe.biografia.lower()
        if any(palabra.lower() in biografia for palabra in palabras):
            resultado.append(heroe.nombre)
    return resultado


# e. Superhéroes que aparecieron antes de un año dado
def heroes_anteriores_a(lista, anio):
    return [(heroe.nombre, heroe.casa) for heroe in lista if heroe.anio_aparicion < anio]


# f. Casa de cada uno de los superhéroes indicados
def casas_de(lista, nombres):
    resultado = {}
    for nombre in nombres:
        heroe = lista.buscar(nombre)
        resultado[nombre] = heroe.casa if heroe is not None else None
    return resultado


# g. Toda la información de los superhéroes indicados
def informacion_de(lista, nombres):
    return [lista.buscar(nombre) for nombre in nombres]


# h. Superhéroes cuyo nombre comienza con alguna de las letras
def heroes_que_comienzan_con(lista, letras):
    letras = tuple(letra.upper() for letra in letras)
    return [heroe.nombre for heroe in lista if heroe.nombre.upper().startswith(letras)]


# i. Cantidad de superhéroes por casa
def contar_por_casa(lista):
    conteo = {}
    for heroe in lista:
        conteo[heroe.casa] = conteo.get(heroe.casa, 0) + 1
    return conteo


def main():
    superheroes = cargar_superheroes()

    print("Lista inicial:")
    for heroe in superheroes:
        print(" -", heroe.nombre)

    print("\na. Eliminar a Linterna Verde")
    eliminado = eliminar_superheroe(superheroes, "Linterna Verde")
    print("   Eliminado:", eliminado.nombre if eliminado else "no encontrado")
    print("   Quedan", len(superheroes), "superhéroes")

    print("\nb. Año de aparición de Wolverine:", anio_de_aparicion(superheroes, "Wolverine"))

    print("\nc. Cambiar la casa de Dr. Strange a Marvel")
    if cambiar_casa(superheroes, "Dr. Strange", "Marvel"):
        print("   Nueva casa:", superheroes.buscar("Dr. Strange").casa)
    else:
        print("   Dr. Strange no está en la lista")

    print("\nd. Superhéroes que mencionan 'traje' o 'armadura' en su biografía:")
    for nombre in heroes_con_palabras_en_biografia(superheroes, ["traje", "armadura"]):
        print(" -", nombre)

    print("\ne. Superhéroes que aparecieron antes de 1963:")
    for nombre, casa in heroes_anteriores_a(superheroes, 1963):
        print(f" - {nombre} ({casa})")

    print("\nf. Casa de Capitana Marvel y Mujer Maravilla:")
    for nombre, casa in casas_de(superheroes, ["Capitana Marvel", "Mujer Maravilla"]).items():
        print(f" - {nombre}: {casa if casa else 'no encontrado'}")

    print("\ng. Información de Flash y Star-Lord:")
    for nombre, heroe in zip(["Flash", "Star-Lord"], informacion_de(superheroes, ["Flash", "Star-Lord"])):
        print(" -", heroe if heroe else f"{nombre}: no encontrado")

    print("\nh. Superhéroes que comienzan con B, M o S:")
    for nombre in heroes_que_comienzan_con(superheroes, ["B", "M", "S"]):
        print(" -", nombre)

    print("\ni. Cantidad de superhéroes por casa:")
    for casa, cantidad in contar_por_casa(superheroes).items():
        print(f" - {casa}: {cantidad}")


if __name__ == "__main__":
    main()
