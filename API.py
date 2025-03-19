from flask import Flask, request, render_template
from Arbol import Nodo
from Puzzle import buscar_solucion_BFS
from a import buscar_solucion_BFS_rec
from lifo import buscar_solucion_DFS

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')  # Renderizar el formulario HTML

@app.route('/resultado', methods=['POST'])
def resultado():
    estado_inicial = list(map(int, request.form.get("estado_inicial", "").split(',')))
    solucion = list(map(int, request.form.get("solucion", "").split(',')))
    algoritmo = request.form.get("algoritmo")

    if algoritmo == "BFS":
        nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    elif algoritmo == "BFS_REC":
        nodo_solucion = buscar_solucion_BFS_rec(Nodo(estado_inicial), solucion, [])
    elif algoritmo =="DFS":
        nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    else:
        return "Método de búsqueda no válido"
    
    # Construir la secuencia de pasos hasta la solución
    resultado = []
    if nodo_solucion:  # Comprobar si se encontró una solución
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
    else:
        resultado = "No se encontró una solución."

    return render_template('resultado.html', resultado=resultado)  # Renderizar el resultado



if __name__ == '__main__':
    app.run(debug=True)
