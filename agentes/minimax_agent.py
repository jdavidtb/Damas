class MinimaxAgent:
    def __init__(self, color='W', depth=3):
        """
        Inicializa el agente Minimax con un color específico y la profundidad de búsqueda.
        
        Parámetros:
            color (str): Color de las piezas que el agente manejará ('W' para blanco, 'B' para negro).
            depth (int): Profundidad del árbol de búsqueda Minimax.
        """
        self.color = color
        self.depth = depth
        self.opponent = 'B' if color == 'W' else 'W'  # Determina automáticamente el color del oponente.

    def choose_move(self, board):
        """
        Elige el mejor movimiento usando el algoritmo Minimax.
        
        Parámetros:
            board (Board): El tablero actual del juego.
            
        Retorna:
            tuple: El mejor movimiento encontrado.
        """
        _, move = self.minimax(board, self.depth, True)
        return move

    def minimax(self, board, depth, maximizing_player):
        """
        Implementa el algoritmo Minimax recursivo para encontrar el mejor movimiento.
        
        Parámetros:
            board (Board): El tablero actual del juego.
            depth (int): Profundidad actual en el árbol de búsqueda.
            maximizing_player (bool): True si este es el turno del jugador maximizador.
        
        Retorna:
            tuple: Una tupla conteniendo el mejor valor de evaluación y el movimiento correspondiente.
        """
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board), None

        best_move = None
        if maximizing_player:
            best_value = float('-inf')
            for move in board.valid_moves(self.color):  # Asegura que solo considera movimientos para el jugador maximizador
                board.apply_move(move)
                eval_value, _ = self.minimax(board, depth - 1, False)
                board.undo_move(move)
                if eval_value > best_value:
                    best_value = eval_value
                    best_move = move
        else:
            best_value = float('inf')
            for move in board.valid_moves(self.opponent):  # Considera movimientos para el jugador minimizador
                board.apply_move(move)
                eval_value, _ = self.minimax(board, depth - 1, True)
                board.undo_move(move)
                if eval_value < best_value:
                    best_value = eval_value
                    best_move = move

        return best_value, best_move

    def evaluate_board(self, board):
        """
        Evalúa el tablero y proporciona una puntuación basada en la posición actual.
        
        Parámetros:
            board (Board): El tablero actual del juego.
            
        Retorna:
            int: La puntuación del tablero.
        """
        my_pieces = sum(1 for row in board.board for piece in row if piece == self.color)
        opp_pieces = sum(1 for row in board.board for piece in row if piece and piece != self.color)
        return my_pieces - opp_pieces
