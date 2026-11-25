class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class listadoble:
    def __init__(self):
        self.inicio= None
        self.final =None

    def insertar_inicio(self,dato):
        nuevo = nodo(dato)
        if self.inicio is None:
            self.inicio =nuevo
            self.final= nuevo
        else :
            nuevo.siguiente=self.inicio
            self.inicio.anterior=nuevo
            self.inicio = nuevo

    def insertar_final(self,dato):
        nuevo=nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo
            self.final = nuevo
        else:
            self.final.siguiente=nuevo
            nuevo.anterior = self.final
            self.final = nuevo

    def imprimir(self):
        actual=self.inicio
        while actual is not None:
            print (actual.dato)
            actual=actual.siguiente
        print ("fin del nodo")
        
tren_nodo = listadoble()
tren_nodo.insertar_final(10)
tren_nodo.insertar_final(20)
tren_nodo.insertar_inicio(30)
tren_nodo.imprimir()