import random
import numpy as np

class QLearningAgent:
    def __init__(self, color='W', alpha=0.5, gamma=0.9, epsilon=0.2):
        """
        Inicializa el agente de Q-Learning.

        Parámetros:
            color (str): Color de las piezas que el agente manejará ('W' para blanco, 'B' para negro).
            alpha (float): Tasa de aprendizaje.
            gamma (float): Factor de descuento.
            epsilon (float): Probabilidad de tomar una acción aleatoria.
        """
        self.color = color
        self.Q = {}  # La tabla Q inicialmente está vacía.
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_move(self, board):
        """
        Decide un movimiento usando la política epsilon-greedy.

        Parámetros:
            board (Board): El tablero actual del juego.

        Retorna:
            tuple: El movimiento elegido.
        """
        state = self.get_state(board)
        if random.random() < self.epsilon:
            # Exploración: Elige un movimiento al azar.
            return random.choice(board.valid_moves(self.color))
        else:
            # Explotación: Elige el mejor movimiento según la tabla Q.
            return self.get_best_move(state, board)

    def get_best_move(self, state, board):
        """
        Obtiene el mejor movimiento según la tabla Q para el estado dado.

        Parámetros:
            state (str): El estado actual del tablero.
            board (Board): El tablero actual del juego.

        Retorna:
            tuple: El mejor movimiento.
        """
        valid_moves = board.valid_moves(self.color)
        if not valid_moves:
            return None
        
        best_move = None
        max_value = float('-inf')
        
        for move in valid_moves:
            next_state = self.get_next_state(board, move)
            q_value = self.Q.get((state, next_state), 0)
            if q_value > max_value:
                max_value = q_value
                best_move = move
        
        return best_move

    def update_q_table(self, old_state, action, reward, new_state):
        """
        Actualiza la tabla Q con la nueva experiencia.

        Parámetros:
            old_state (str): El estado anterior.
            action (tuple): La acción realizada.
            reward (int): La recompensa recibida.
            new_state (str): El nuevo estado después de la acción.
        """
        old_value = self.Q.get((old_state, new_state), 0)
        future_rewards = max(self.Q.get((new_state, next_state), 0) for next_state in self.get_all_possible_next_states(new_state))
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * future_rewards)
        self.Q[(old_state, new_state)] = new_value

    def get_state(self, board):
        """
        Convierte el tablero actual en un estado comprensible para el agente.

        Parámetros:
            board (Board): El tablero actual del juego.

        Retorna:
            str: Una representación en cadena del estado del tablero.
        """
        return str(board.board)

    def get_next_state(self, board, move):
        """
        Simula el tablero después de un movimiento y retorna el nuevo estado.

        Parámetros:
            board (Board): El tablero actual.
            move (tuple): El movimiento propuesto.

        Retorna:
            str: El nuevo estado del tablero después del movimiento.
        """
        board.apply_move(move)
        state = str(board.board)
        board.undo_move(move)
        return state

    def get_all_possible_next_states(self, board):
        """
        Genera todos los posibles estados futuros desde el estado actual del tablero.

        Parámetros:
            board (Board): El tablero actual.

        Retorna:
            list: Lista de todos los estados posibles.
        """
        all_possible_states = []
        current_state = self.get_state(board)  # Obtiene el estado actual como una cadena

        # Obtiene todos los movimientos válidos para el jugador actual
        valid_moves = board.valid_moves(self.color)
        for move in valid_moves:
            # Aplica cada movimiento para simular el estado resultante
            board.apply_move(move)
            new_state = self.get_state(board)
            all_possible_states.append(new_state)

            # Deshacer el movimiento para restaurar el tablero a su estado original
            board.undo_move(move)

        return all_possible_states

    def reward(self, board, move, result):
        """
        Calcula la recompensa para un movimiento dado.

        Parámetros:
            board (Board): El tablero en el estado antes de aplicar el movimiento.
            move (tuple): El movimiento realizado.
            result (str): El resultado del movimiento ('win', 'loss', 'continue').

        Retorna:
            int: La recompensa asignada al movimiento.
        """
        # Inicializamos la recompensa base
        reward = 0

        # Calculamos cambios en el número de piezas
        initial_pieces = sum(1 for row in board.board for piece in row if piece == self.color)
        board.apply_move(move)
        final_pieces = sum(1 for row in board.board for piece in row if piece == self.color)
        opponent_initial_pieces = sum(1 for row in board.board for piece in row if piece == self.opponent)
        opponent_final_pieces = sum(1 for row in board.board for piece in row if piece == self.opponent)

        # Asigna recompensa por capturar piezas del oponente
        if opponent_final_pieces < opponent_initial_pieces:
            reward += (opponent_initial_pieces - opponent_final_pieces) * 100

        # Asigna penalización por perder piezas
        if final_pieces < initial_pieces:
            reward -= (initial_pieces - final_pieces) * 50

        # Asigna recompensa por ganar o penalización por perder
        if result == 'win':
            reward += 500  # Recompensa grande por ganar el juego
        elif result == 'loss':
            reward -= 500  # Penalización grande por perder el juego

        # Revertir el movimiento para restaurar el estado del tablero
        board.undo_move(move)

        return reward

    def __str__(self):
        return f"QLearningAgent({self.color})"
