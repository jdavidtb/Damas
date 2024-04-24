import random
from game.board import Board

class RandomAgent:
    def __init__(self, color='W'):
        """
        Inicializa el agente con un color específico.
        Color 'W' para blanco y 'B' para negro.
        """
        self.color = color

    def choose_move(self, board):
        """
        Elige un movimiento al azar de la lista de movimientos válidos.
        
        Parámetros:
            board (Board): Instancia actual del tablero de juego.
            
        Retorna:
            tuple: Movimiento seleccionado al azar (coordenada inicial y final).
        """
        valid_moves = self.get_valid_moves(board)
        if valid_moves:
            return random.choice(valid_moves)
        else:
            return None

    def get_valid_moves(self, board):
        """
        Filtra y retorna todos los movimientos válidos para el color del agente.
        
        Parámetros:
            board (Board): Instancia del tablero desde donde se extraerán los movimientos válidos.
            
        Retorna:
            list: Lista de movimientos válidos.
        """
        moves = board.valid_moves()
        color_moves = [move for move in moves if board.board[move[0][0]][move[0][1]] == self.color]
        return color_moves

    def __str__(self):
        return f"RandomAgent({self.color})"
