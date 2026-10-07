class Nodo:
    """Nodo de una lista enlazada simple."""

    def __init__(self, info):
        self.info = info
        self.siguiente = None


class Lista:
    """Lista enlazada simple ordenada.

    El criterio es una función que, dado un elemento, devuelve la clave
    por la que se ordena y se busca (por ejemplo, el nombre del superhéroe).
    """

    def __init__(self, criterio=None):
        self.__inicio = None
        self.__tamanio = 0
        self.__criterio = criterio if criterio is not None else (lambda dato: dato)

    def esta_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def __len__(self):
        return self.__tamanio

    def insertar(self, dato):
        """Inserta el dato manteniendo la lista ordenada según el criterio."""
        nuevo = Nodo(dato)
        clave = self.__criterio(dato)

        if self.__inicio is None or clave < self.__criterio(self.__inicio.info):
            nuevo.siguiente = self.__inicio
            self.__inicio = nuevo
        else:
            anterior = self.__inicio
            actual = self.__inicio.siguiente
            while actual is not None and self.__criterio(actual.info) <= clave:
                anterior = actual
                actual = actual.siguiente
            nuevo.siguiente = actual
            anterior.siguiente = nuevo

        self.__tamanio += 1

    def eliminar(self, clave):
        """Elimina el primer nodo cuya clave coincida. Devuelve el dato eliminado o None."""
        anterior = None
        actual = self.__inicio
        while actual is not None and self.__criterio(actual.info) != clave:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return None

        if anterior is None:
            self.__inicio = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        self.__tamanio -= 1
        return actual.info

    def buscar(self, clave):
        """Devuelve el dato cuya clave coincida, o None si no está."""
        actual = self.__inicio
        while actual is not None and self.__criterio(actual.info) != clave:
            actual = actual.siguiente
        return actual.info if actual is not None else None

    def __iter__(self):
        """Permite recorrer la lista con un for."""
        actual = self.__inicio
        while actual is not None:
            yield actual.info
            actual = actual.siguiente
