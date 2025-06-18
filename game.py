import pygame
from board import Board
from ai import *

class Game:
    def __init__(self, win, is_ai=False):
        self._init()
        self.win = win
        self.vs_ai = is_ai

    def ai_move(self):
        board, _ = minimax(self.board, 2, False, self)
        self.board = board
        self.change_turn()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = 'white'
        self.valid_moves = {}
        self.SQUARE_SIZE = 80

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        """piece = self.board.get_piece(row, col)"""
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        self.turn = 'black' if self.turn == 'white' else 'white'

    def check_winner(self):
        white_left = any(piece for row in self.board.board for piece in row if piece != 0 and piece.color == 'white')
        black_left = any(piece for row in self.board.board for piece in row if piece != 0 and piece.color == 'black')

        if not white_left:
            return 'black'
        if not black_left:
            return 'white'
        return None
