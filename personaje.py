ROMANOS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}


def a_romano(episodio):
    return ROMANOS.get(episodio, str(episodio))


class Personaje:
    """Personaje de la saga de Star Wars."""

    def __init__(self, nombre, altura, edad, genero, especie, planeta_natal, episodios):
        self.nombre = nombre
        self.altura = altura              # en centímetros
        self.edad = edad                  # en años
        self.genero = genero
        self.especie = especie
        self.planeta_natal = planeta_natal
        self.episodios = episodios        # lista de números de episodio

    def episodios_romanos(self):
        return ", ".join(a_romano(episodio) for episodio in self.episodios)

    def __str__(self):
        return (f"{self.nombre} | Altura: {self.altura} cm | Edad: {self.edad} | "
                f"Género: {self.genero} | Especie: {self.especie} | "
                f"Planeta: {self.planeta_natal} | Episodios: {self.episodios_romanos()}")
