import unittest
from chessAI.model.play.factory import PlayerFactory
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator
from chessAI.util.error import MissingParameterError


class PlayerFactoryTest(unittest.TestCase):

    def test_missing_class_name(self):

        parameters = {}
        self.assertRaises(MissingParameterError, PlayerFactory.create_player, parameters)

    def test_create_player_1(self):

        parameters = {
            'class': 'ShallowPlayer',
            'evaluator': {
                'class': 'SimpleFCNEvaluator'
            }
        }

        player = PlayerFactory.create_player(parameters)
        self.assertIsInstance(player, ShallowPlayer)
        self.assertIsInstance(player.evaluator, SimpleFCNEvaluator)
