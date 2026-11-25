class Nodo: #clase principal
    def __init__(self,dato): #funcion dentro de la clase
        self.dato = dato #variable en la funcion
        self.siguiente = None #punntero al siguiente nodo
class lista_enlazada: 
    def __init__(self): #init significa que inicializa una sola vez
        self.cabeza = None #El inicio de la lista en empieza con 0 datos
    def insertar(self,dato):
        
        nuevo = Nodo(dato)
        if self.cabeza is None: #si el nodo esta vacio entonces entra a la opcion verdadera
            self.cabeza = nuevo #este nodo se convierte en el primero
            return
        actual = self.cabeza #si a hay nodos nos paramos en el primero o la cabeza

        while actual.siguiente is not None: # mientras haya un nodo nos conectamos adelante
            actual = actual.siguiente #camina al siguiente nodo
        actual.siguiente = nuevo #ya estamos en el ultimo nodo, hacemos su apuntador señale al

    def imprimir(self): 
        actual= self.cabeza 
        while actual is not None:
            print(actual.dato)
            actual= actual.siguiente
        print ("fin de la lista")

mi_lista = lista_enlazada()
mi_lista.insertar(10)
mi_lista.insertar(20)
mi_lista.insertar(30)
mi_lista.imprimir()