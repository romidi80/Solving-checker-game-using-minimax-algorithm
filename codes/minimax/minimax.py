from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, maxPlayer, game):

    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if maxPlayer == True:
        maxEval = float("-inf")
        best_move = None
        for move in getAllMoves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
           
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move

    else:
        minEval = float("inf")
        best_move = None
        for move in getAllMoves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulateMove(piece, move, board, game, skip):

    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def getAllMoves(board, color, game):

    moves = []   
    for piece in board.getAllPieces(color):
        valid_moves = board.getValidMoves(piece)

        for move, skip in valid_moves.items():
            previous_board = deepcopy(board)
            previous_piece = previous_board.getPiece(piece.row, piece.col)
            new_board = simulateMove(previous_piece, move, previous_board, game, skip)
            moves.append(new_board)

    return moves