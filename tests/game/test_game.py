import unittest
import chess

from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator
from config import config
from chessAI.game.engine import EnginePlayer
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.game.game import Game


class GameTest(unittest.TestCase):

    def test_engine_vs_model_game(self):

        engine_path = config['test']['uci_engine_path']
        player_1 = EnginePlayer(engine_path, time_limit=0.1)

        evaluator = SimpleCNNEvaluator()
        player_2 = ShallowPlayer(evaluator)

        board = chess.Board()
        game = Game(player_1, player_2, board)
        result = game.run()

        self.assertIsInstance(result, dict)
        self.assertIn('score', result)
        self.assertIn('reason', result)
        self.assertIn('nth_move', result)
        self.assertIn(result['score'], (0, 0.5, 1))
        self.assertIsNotNone(result['reason'])
        self.assertIsInstance(result['nth_move'], int)
