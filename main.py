class Nodo:
    def __init__(self, elemento, siguiente=None):
        self.elemento = elemento
        self.siguiente = siguiente


class ColaDinamica:
    def __init__(self):
        self.primero_nodo = None
        self.ultimo_nodo = None
        self.tamanio = 0

    # Indica si la cola está vacía
    def is_empty(self):
        return self.primero_nodo is None

    # Devuelve el tamaño de la cola
    def size(self):
        return self.tamanio

    # Devuelve el primer elemento sin quitarlo
    def primero(self):
        if self.is_empty():
            return None
        return self.primero_nodo.elemento

    # Quita el primer elemento y lo devuelve
    def dequeue(self):
        if self.is_empty():
            return None

        elemento = self.primero_nodo.elemento
        self.primero_nodo = self.primero_nodo.siguiente
        self.tamanio -= 1

        if self.is_empty():
            self.ultimo_nodo = None

        return elemento

    # Inserta un elemento y lo devuelve
    def enqueue(self, elemento):
        aux = Nodo(elemento)

        if self.is_empty():
            self.primero_nodo = aux
            self.ultimo_nodo = aux
        else:
            if self.tamanio == 1:
                self.primero_nodo.siguiente = aux
            else:
                self.ultimo_nodo.siguiente = aux
            self.ultimo_nodo = aux

        self.tamanio += 1
        return aux.elemento

    def __str__(self):
        if self.is_empty():
            return "La cola está vacía"
        cadena = ""
        actual = self.primero_nodo
        while actual is not None:
            cadena += f"[{actual.elemento}] "
            actual = actual.siguiente
        return cadena


# --- SIMULACIÓN DE GESTIÓN DE TURNOS ---
if __name__ == "__main__":
    cola_turnos = ColaDinamica()

    print("=== SISTEMA DE GESTIÓN DE TURNOS ===")
    print(f"¿Está vacía?: {cola_turnos.is_empty()}")
    print(f"Tamaño inicial: {cola_turnos.size()}\n")

    print("--- Registrar turnos ---")
    print("Registrado:", cola_turnos.enqueue("Turno A-01: Carlos"))
    print("Registrado:", cola_turnos.enqueue("Turno A-02: María"))
    print("Registrado:", cola_turnos.enqueue("Turno A-03: Juan"))
    print("Registrado:", cola_turnos.enqueue("Turno A-04: Ana"))
    print()

    print("Estado actual:", cola_turnos)
    print("Tamaño:", cola_turnos.size())
    print("Siguiente en atender:", cola_turnos.primero())
    print()

    print("--- Atender turnos ---")
    print("Atendiendo a:", cola_turnos.dequeue())
    print("Atendiendo a:", cola_turnos.dequeue())
    print()

    print("Estado tras atender 2 turnos:", cola_turnos)
    print("Siguiente:", cola_turnos.primero())
    print("Pendientes:", cola_turnos.size())
    print()

    print("--- Finalizar cola ---")
    print("Atendiendo a:", cola_turnos.dequeue())
    print("Atendiendo a:", cola_turnos.dequeue())
    print("Intentar atender vacía:", cola_turnos.dequeue())
    print()

    print(f"¿Está vacía?: {cola_turnos.is_empty()}")
    print(f"Tamaño final: {cola_turnos.size()}")