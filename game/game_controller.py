import turtle
from game.board import Board

class GameController:
    def __init__(self, board, player1, player2):
        """
        Inicializa el controlador del juego con un tablero y dos jugadores.

        Parámetros:
            board (Board): La instancia del tablero de juego.
            player1, player2: Los dos agentes que participarán en el juego.
        """
        self.board = board
        self.players = { 'W': player1, 'B': player2 }
        self.current_turn = 'W'  # Blanco comienza por defecto

    def play(self):
        """
        Comienza y maneja el juego hasta que termine.
        """
        game_over = False
        while not game_over:
            self.board.update_board()
            current_player = self.players[self.current_turn]
            move = current_player.choose_move(self.board)
            if move:
                self.board.apply_move(move)
                game_over = self.board.is_game_over()
                self.current_turn = 'B' if self.current_turn == 'W' else 'W'
            else:
                print(f"No hay movimientos válidos para {self.current_turn}. Cambio de turno.")
                self.current_turn = 'B' if self.current_turn == 'W' else 'W'
                game_over = self.board.is_game_over()
        
        self.end_game()

    def end_game(self):
        """
        Finaliza el juego mostrando el resultado y cerrando la ventana de Turtle.
        """
        winner = 'Ninguno'  
        if self.board.count_pieces('W') > self.board.count_pieces('B'):
            winner = 'Blanco'
        elif self.board.count_pieces('B') > self.board.count_pieces('W'):
            winner = 'Negro'

        print(f"Juego terminado. Ganador: {winner}")
        turtle.mainloop()  # Mantener la ventana abierta hasta que el usuario decida cerrarla

