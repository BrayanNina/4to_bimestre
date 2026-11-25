class Nodo:
    def _init_(self, codigo):
        self.codigo = codigo
        self.siguiente = None

class ListaSimple:
    def _init_(self):
        self.cabeza = None

    def registrar(self, codigo):
        nuevo = Nodo(codigo)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        print("Pedido registrado correctamente.")

    def cancelar(self):
        if self.cabeza is None:
            print("No hay pedidos para cancelar.")
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
        else:
            actual = self.cabeza

            while actual.siguiente.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = None

        print("Ultimo pedido cancelado.")

    def mostrar(self):
        if self.cabeza is None:
            print("No hay pedidos registrados.")
            return

        actual = self.cabeza
        print("Pedidos actuales:")

        while actual is not None:
            print(actual.codigo, end=" -> ")
            actual = actual.siguiente

        print("None")

lista = ListaSimple()

while True:
    print("\n===== MENU DE PEDIDOS =====")
    print("1. Registrar nuevo pedido")
    print("2. Cancelar ultimo pedido")
    print("3. Mostrar pedidos")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        codigo = int(input("Ingrese el codigo del pedido: "))
        lista.registrar(codigo)

    elif opcion == "2":
        lista.cancelar()

    elif opcion == "3":
        lista.mostrar()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida.")