import unittest
import chess
from chessAI.model.representation.volume import VolumeRepresentation
from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator


class SimpleCNNEvaluatorTest(unittest.TestCase):

    def test_simple_cnn_evaluator(self):

        board = chess.Board()
        volume_representation = VolumeRepresentation.from_board(board)
        sce = SimpleCNNEvaluator()
        score = sce.evaluate(volume_representation)
        self.assertIsInstance(score, float)
