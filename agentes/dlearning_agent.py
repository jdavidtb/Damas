import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from game.board import Board

class DLearningAgent:
    def __init__(self, color='W', learning_rate=0.001):
        self.color = color
        self.model = self.build_model()
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        self.loss_function = nn.MSELoss()

    def build_model(self):
        model = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, 1)
        )
        return model

    def choose_move(self, board):
        valid_moves = board.valid_moves(self.color)
        best_move = None
        max_value = float('-inf')
        for move in valid_moves:
            board.apply_move(move)
            state_value = self.evaluate_board(board)
            board.undo_move(move)
            if state_value > max_value:
                max_value = state_value
                best_move = move
        return best_move

    def evaluate_board(self, board):
        state = self.board_to_input(board)
        state_tensor = torch.tensor(state, dtype=torch.float32)
        self.model.eval()
        with torch.no_grad():
            value = self.model(state_tensor)
        return value.item()

    def board_to_input(self, board):
        state = np.zeros(64, dtype=float)
        for i in range(8):
            for j in range(8):
                piece = board.board[i][j]
                if piece == self.color:
                    state[i * 8 + j] = 1.0
                elif piece:
                    state[i * 8 + j] = -1.0
        return state

    def train(self, epochs, num_games_per_epoch):
        for epoch in range(epochs):
            total_loss = 0
            for _ in range(num_games_per_epoch):
                board = Board()
                while not board.is_game_over():
                    move = self.choose_move(board)
                    board.apply_move(move)
                result = board.result()
                target_value = 1 if result == self.color else -1
                self.optimizer.zero_grad()
                current_value = self.evaluate_board(board)
                loss = self.loss_function(torch.tensor([current_value], dtype=torch.float32), torch.tensor([target_value], dtype=torch.float32))
                loss.backward()
                self.optimizer.step()
                total_loss += loss.item()
            print(f'Epoch {epoch+1}, Loss: {total_loss / num_games_per_epoch}')

if __name__ == '__main__':
    agent = DLearningAgent(color='W')
    agent.train(epochs=10, num_games_per_epoch=100)
