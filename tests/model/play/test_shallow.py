import unittest
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator
from chess import Board, Move

class RankMovesTest(unittest.TestCase):

    def test_get_highest_ranked_move(self):

        random_evaluator = SimpleCNNEvaluator()
        player = ShallowPlayer(random_evaluator)
        board = Board()
        move, score = player.get_highest_ranked_move(board)
        self.assertIsInstance(score, float)
        self.assertIsInstance(move, Move)
