
# Buscar desde la cabeza
def buscar(dato):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == dato:
            return True

        actual = actual["siguiente"]

    return False


# Buscar desde la cola
def buscar_atras(dato):
    actual = cola

    while actual is not None:
        if actual["dato"] == dato:
            return True

        actual = actual["anterior"]

    return False
