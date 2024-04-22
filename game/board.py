import turtle
from game.board import *
class Board:
    def __init__(self):
        self.board = self.create_initial_board()
        self.setup_board()

    def create_initial_board(self):
        # Crear un tablero 8x8 con 'None' donde no hay piezas
        board = [[None for _ in range(8)] for _ in range(8)]
        # Colocar las piezas de los jugadores
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        board[i][j] = 'B'  # 'B' para piezas negras
                    elif i > 4:
                        board[i][j] = 'W'  # 'W' para piezas blancas
        return board

    def setup_board(self):
        turtle.speed(0)
        turtle.hideturtle()
        side_length = 50
        for row in range(8):
            for col in range(8):
                color = 'black' if (row + col) % 2 == 1 else 'white'
                start_x = col * side_length - 200
                start_y = -row * side_length + 200
                self.draw_square(color, start_x, start_y, side_length)
        self.place_pieces()

    def draw_square(self, color, start_x, start_y, side_length):
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(side_length)
            turtle.right(90)
        turtle.end_fill()

    def place_pieces(self):
        side_length = 50
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    turtle.penup()
                    turtle.goto(j * side_length - 200 + side_length // 2, -i * side_length + 200 - side_length // 2)
                    turtle.pendown()
                    turtle.color('red' if piece == 'W' else 'gray')
                    turtle.begin_fill()
                    turtle.circle(side_length // 2)
                    turtle.end_fill()

    def apply_move(self, move):
        # Actualizar el tablero y luego visualizar los cambios
        (x1, y1), (x2, y2) = move
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = None
        # Captura simple por salto
        if abs(x2 - x1) == 2:
            self.board[(x1 + x2) // 2][(y1 + y2) // 2] = None
        self.update_board()

    def update_board(self):
        # Actualiza la visualización del tablero
        turtle.clear()
        self.setup_board()

    def valid_moves(self):
        # Calcular movimientos válidos, implementación básica
        moves = []
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    direction = -1 if piece == 'W' else 1
                    for dx in [-1, 1]:
                        ni, nj = i + direction, j + dx
                        if 0 <= ni < 8 and 0 <= nj < 8 and not self.board[ni][nj]:
                            moves.append(((i, j), (ni, nj)))
        return moves

    def is_game_over(self):
        # Verificar si el juego ha terminado
        return not self.valid_moves()
