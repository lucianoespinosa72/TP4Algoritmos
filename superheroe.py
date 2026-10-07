class Superheroe:
    """Superhéroe de cómic."""

    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"{self.nombre} | Año: {self.anio_aparicion} | Casa: {self.casa}\n"
                f"    Biografía: {self.biografia}")
