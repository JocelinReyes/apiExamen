from Arbol import Nodo;

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while not solucionado and nodos_frontera:
        nodo = nodos_frontera.pop()  # Cambio de pop(0) a pop() para implementar LIFO
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo  # Se encontró la solución

        dato_nodo = nodo.get_datos()

        # Operador Izquierdo (intercambiar posición 0 y 1)
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_izquierdo.padre = nodo
        if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_izquierdo)

        # Operador Centro (intercambiar posición 1 y 2)
        hijo_centro = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_centro.padre = nodo
        if not hijo_centro.en_lista(nodos_visitados) and not hijo_centro.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_centro)

        # Operador Derecha (intercambiar posición 2 y 3)
        hijo_derecha = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        hijo_derecha.padre = nodo
        if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_derecha)
    
    return None  # No se encontró solución

if __name__ == "__main__":
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
