import turtle

class Board:
    def __init__(self):
        self.board = [[' ']*8 for _ in range(8)]
        self.initialize_board()
        turtle.speed(0)
        turtle.hideturtle()
        self.side_length = 50
        self.setup_board()

    def initialize_board(self):
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 != 0:
                    self.board[i][j] = 'B'
        
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    self.board[i][j] = 'W'

    def setup_board(self):
        for row in range(8):
            for col in range(8):
                color = 'black' if (row + col) % 2 == 1 else 'white'
                start_x = col * self.side_length - 200
                start_y = -row * self.side_length + 200
                self.draw_square(color, start_x, start_y)
        self.place_pieces()

    def draw_square(self, color, start_x, start_y):
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.side_length)
            turtle.right(90)
        turtle.end_fill()

    def place_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece != ' ':
                    turtle.penup()
                    turtle.goto(j * self.side_length - 200 + self.side_length // 2, -i * self.side_length + 200 - self.side_length // 2)
                    turtle.pendown()
                    turtle.color('red' if piece == '○' else 'gray')
                    turtle.begin_fill()
                    turtle.circle(self.side_length // 2)
                    turtle.end_fill()

    def is_valid_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False
        if self.board[end_row][end_col] != ' ':
            return False
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False
        if self.board[start_row][start_col] == 'B' and end_row <= start_row:
            return False
        if self.board[start_row][start_col] == 'W' and end_row >= start_row:
            return False
        return True

    def make_move(self, start, end):
        if self.is_valid_move(start, end):
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = ' '
            self.update_board()

    def update_board(self):
        turtle.clear()
        self.setup_board()

    def play(self):
        self.update_board()
        print("Setup complete. Game can be played with manual inputs.")
