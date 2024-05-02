from agentes.minimax_agent import MinimaxAgent
from game.board import Board
from utilities import medir_profundidad_minimax

def test_minimax_depth():
    test_board = Board()  
    test_agent = MinimaxAgent('W', depth=3)
    profundidad_optima = medir_profundidad_minimax(test_agent, test_board)
    print(f"Profundidad óptima alcanzada: {profundidad_optima}")

if __name__ == "__main__":
    test_minimax_depth()
