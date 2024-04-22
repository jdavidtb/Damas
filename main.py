import turtle
from game.board import Board

def choose_agent():
    print("Selecciona el agente para el jugador:")
    print("1. Agente Random")
    print("2. Agente Minimax")
    print("3. Agente Q-Learning")
    print("4. Agente Deep Learning")
    choice = int(input("Ingresa el número del agente: "))

    if choice == 1:
        return RandomAgent()
    elif choice == 2:
        return MinimaxAgent(depth=3)  
    elif choice == 3:
        return QLearningAgent()
    elif choice == 4:
        return DeepLearningAgent()
    else:
        print("Selección no válida. Usando Agente Random por defecto.")
        return RandomAgent()
def main():
    # Configura la ventana de Turtle
    turtle.setup(500, 500)
    turtle.title("Juego de Damas")

    # Permite a los usuarios elegir los agentes
    player1 = choose_agent()
    player2 = choose_agent()  

    # Crea e inicializa el tablero de damas
    game_board = Board()
    game = Game(game_board, player1, player2)  # Asume que la clase Game gestiona los turnos y el juego

    # Inicia el juego
    game.play()  # Asume que esta función gestiona el bucle del juego y la lógica de turnos

    # Mantiene la ventana abierta hasta que se cierre manualmente
    turtle.done()

if __name__ == "__main__":
    main()