import numpy as np
import chess
import chess.engine
from chessAI.model.play.base import Player


class EnginePlayer(Player):

    def __init__(self, engine_path, time_limit):
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path, timeout=10)
        self.time_limit = time_limit

    def play(self, board, **kwargs):
        play_result = self.engine.play(board, chess.engine.Limit(time=self.time_limit))
        result = {
            'move': play_result.move,
            'resigned': play_result.resigned
        }
        return result

    def close(self):
        self.engine.quit()


class RandomPlayer(Player):

    def play(self, board, **kwargs):
        legal_moves = list(board.legal_moves)
        random_move = np.random.choice(legal_moves, 1)
        result = {
            'move': random_move,
            'resigned': False
        }
        return result

    def close(self):
        pass
