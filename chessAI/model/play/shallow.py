import copy

from chessAI.model.representation.volume import VolumeRepresentation
from .base import Player


class ShallowPlayer(Player):
    """
    Evaluates the best move by evaluating all possible legal moves and returning the one resulting in a board with the
    highest evaluation score.
    """

    def __init__(self, evaluator):
        self.evaluator = evaluator

    def get_highest_ranked_move(self, board, side=0):

        highest_ranked_move = None
        evaluation_score = None

        legal_moves = board.legal_moves
        for move in legal_moves:
            next_board = copy.deepcopy(board)
            next_board.push(move)
            volume_representation = VolumeRepresentation.from_board(next_board)
            score = self.evaluator.evaluate(volume_representation)

            side_score = score * (-1)**(side != 0)
            if highest_ranked_move is None or side_score > evaluation_score:
                highest_ranked_move = move
                evaluation_score = side_score

        return highest_ranked_move, evaluation_score
