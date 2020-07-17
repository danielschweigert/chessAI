import unittest
import chess

from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator
from config import config
from chessAI.model.play.engine import EnginePlayer
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.game.game import Game, Series


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
        player_1.close()
        player_2.close()


class SeriesTest(unittest.TestCase):

    def test_series(self):

        engine_path = config['test']['uci_engine_path']
        player_1 = EnginePlayer(engine_path, time_limit=0.1)

        evaluator = SimpleCNNEvaluator()
        player_2 = ShallowPlayer(evaluator)

        initial_boards = [chess.Board()]
        n_rounds = 10

        series = Series(player_1=player_1,
                        player_2=player_2,
                        initial_boards=initial_boards,
                        n_rounds=n_rounds)

        result = series.run()
        self.assertEqual(n_rounds * len(initial_boards), result['rounds_completed'])
        self.assertIsInstance(result['reasons'], dict)
        self.assertIsInstance(result['scores'], dict)

        null_sum = result['scores']['player_1']['total'] \
                   + result['scores']['player_2']['total'] \
                   - result['scores']['player_1']['n_draws'] * 0.5
        self.assertEqual(0, null_sum)

        player_1.close()
        player_2.close()
