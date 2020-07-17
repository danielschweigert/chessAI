import unittest
import chess
from chessAI.model.play.engine import RandomPlayer


class RandomPlayerTest(unittest.TestCase):

    def test_random_player(self):
        random_player = RandomPlayer()
        board = chess.Board()
        play_result = random_player.play(board)

        self.assertIn('move', play_result)
        self.assertIn('resigned', play_result)

        self.assertIn(play_result['move'], list(board.legal_moves))
        self.assertEqual(False, play_result['resigned'])
