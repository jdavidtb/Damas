import time

def medir_profundidad_minimax(agent, board, tiempo_maximo=10):
    """
    Mide la máxima profundidad de búsqueda que Minimax puede alcanzar en un tiempo determinado.
    
    Parámetros:
        agent (MinimaxAgent): El agente que ejecuta el algoritmo Minimax.
        board (Board): El tablero de juego actual sobre el que se ejecuta Minimax.
        tiempo_maximo (int): El máximo número de segundos para ejecutar la prueba.
    
    Retorna:
        int: La máxima profundidad alcanzada dentro del límite de tiempo.
    """
    profundidad = 1
    mejor_profundidad = 0
    tiempo_inicial = time.time()

    # Incrementa la profundidad hasta que el tiempo de ejecución exceda el tiempo máximo permitido
    while True:
        tiempo_inicio_prueba = time.time()
        agent.minimax(board, profundidad, True)  # Asume que el agente maximiza primero
        tiempo_prueba = time.time() - tiempo_inicio_prueba
        
        # Comprueba si el tiempo total excedió el tiempo máximo después de agregar el último tiempo de prueba
        if (time.time() - tiempo_inicial + tiempo_prueba) > tiempo_maximo:
            break
        
        mejor_profundidad = profundidad
        profundidad += 1

    return mejor_profundidad
