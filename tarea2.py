class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaDoble:
    def __init__(self):
        self.inicio= None
        self.fin =None

    def insertar_inicio(self,dato):
        nuevo = nodo(dato)
        if self.inicio is None:
           self.inicio =nuevo
           self.fin= nuevo
        else :
           nuevo.siguiente=self.inicio
           self.inicio.anterior=nuevo
           self.inicio = nuevo
    def insertar_final(self,dato):
        nuevo=nodo(dato)
        if self.inicio is None:
           self.inicio = nuevo
           self.fin = nuevo
        else:
            self.final.siguiente=nuevo
            nuevo.anterior = self.final
            self.fin = nuevo
    def mostrar_inicio(self):
        if self.inicio is None:
            print ("la lista esta vacia")
            return
        actual = self.inicio
        print ("lista de inicio a fin")

        while actual is not None:
            print ("actual.dato, end=<->")
            actual = actual.siguiente
        print ("None")

    def mostrar_final(self):
        if self.inicio is None:
            print ("la lista esta vacia")
            return
        actual = self.fin
        print ("lista de fin a inicio")
    
        while actual is not None:
            print ("actual.dato, end=<->")
            actual = actual.anterior
        print ("None")

lista = ListaDoble()
while True:
    print("\n===== MENU LISTA DOBLEMENTE ENLAZADA =====")
    print("1. Insertar numero al inicio")
    print("2. Insertar numero al final")
    print("3. Mostrar del inicio al final")
    print("4. Mostrar del final al inicio")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        numero = int(input("Ingrese un numero entero: "))
        lista.insertar_inicio(numero)

    elif opcion == "2":
        numero = int(input("Ingrese un numero entero: "))
        lista.insertar_final(numero)

    elif opcion == "3":
        lista.mostrar_inicio()

    elif opcion == "4":
        lista.mostrar_final()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida.")
