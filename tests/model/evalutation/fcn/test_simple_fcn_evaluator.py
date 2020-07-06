import unittest
import chess
import torch
from chessAI.model.representation.volume import VolumeRepresentation
from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator


class SimpleFCNEvaluatorTest(unittest.TestCase):

    def test_simple_cnn_evaluator(self):

        board = chess.Board()
        volume_representation = VolumeRepresentation.from_board(board)
        sfe = SimpleFCNEvaluator()
        score = sfe.evaluate(volume_representation)
        self.assertIsInstance(score, float)

    def test_get_set_parameters(self):
        sfe = SimpleFCNEvaluator()
        parameters = sfe.get_parameters()
        n_parameters = parameters.shape[0]
        new_vector = torch.arange(n_parameters)
        sfe.set_parameters(new_vector)
        self.assertEqual(list(new_vector.detach().numpy()), list(sfe.get_parameters()))
