import unittest
import chess
import torch
from chessAI.model.representation.volume import VolumeRepresentation
from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator


class SimpleCNNEvaluatorTest(unittest.TestCase):

    def test_simple_cnn_evaluator(self):

        board = chess.Board()
        volume_representation = VolumeRepresentation.from_board(board)
        sce = SimpleCNNEvaluator()
        score = sce.evaluate(volume_representation)
        self.assertIsInstance(score, float)

    def test_get_set_parameters(self):
        sce = SimpleCNNEvaluator()
        parameters = sce.get_parameters()
        n_parameters = parameters.shape[0]
        new_vector = torch.arange(n_parameters)
        sce.set_parameters(new_vector)
        self.assertEqual(list(new_vector), list(sce.get_parameters()))
