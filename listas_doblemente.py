cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo

agregar_final("Inicio")
agregar_final("Catálogo")
agregar_final("Contacto")

def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["siguiente"] else "\n")
        actual = actual["siguiente"]

def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["anterior"] else "\n")
        actual = actual["anterior"]

mostrar_adelante()
mostrar_atras()

def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = cola = nuevo
    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo

agregar_inicio("Bienvenida")
mostrar_adelante()
mostrar_atras()