import copy
from board import Board

def minimax(position, depth, max_player, game):
    if depth == 0:
        return position, evaluate(position)

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, 'white', game):
            evaluation = minimax(move, depth-1, False, game)[1]
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
        return best_move, max_eval
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, 'black', game):
            evaluation = minimax(move, depth-1, True, game)[1]
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
        return best_move, min_eval

def evaluate(board):
    white_score = black_score = 0
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == 'white':
                    white_score += 2 if piece.king else 1
                else:
                    black_score += 2 if piece.king else 1
    return white_score - black_score

def get_all_moves(board, color, game):
    moves = []
    for row in board.board:
        for piece in row:
            if piece != 0 and piece.color == color:
                valid_moves = board.get_valid_moves(piece)
                for move, skip in valid_moves.items():
                    temp_board = copy.deepcopy(board)
                    temp_piece = temp_board.get_piece(piece.row, piece.col)
                    temp_board.move(temp_piece, move[0], move[1])
                    if skip:
                        temp_board.remove(skip)
                    moves.append(temp_board)
    return moves
