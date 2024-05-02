import turtle
from game.board import Board
from agentes.random_agent import RandomAgent
from agentes.minimax_agent import MinimaxAgent
from agentes.qlearning_agent import QLearningAgent
from agentes.dlearning_agent import DeepLearningAgent  
from game.game_controller import GameController
def choose_agent():
    print("Selecciona el agente para el jugador:")
    print("1. Agente Random")
    print("2. Agente Minimax")
    print("3. Agente Q-Learning")
    print("4. Agente Deep Learning")
    while True:
        try:
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
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

def main():
    # Configura la ventana de Turtle
    turtle.setup(500, 500)
    turtle.title("Juego de Damas")

    # Permite a los usuarios elegir los agentes
    player1 = choose_agent()
    player2 = choose_agent()

    # Crea e inicializa el tablero de damas
    game_board = Board()
    game = GameController(game_board, player1, player2)  # Asume que la clase Game gestiona los turnos y el juego

    # Inicia el juego
    game.play()

    # Mantiene la ventana abierta hasta que se cierre manualmente
    turtle.done()

if __name__ == "__main__":
    main()
