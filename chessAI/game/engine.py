import chess
import chess.engine


class EnginePlayer:

    def __init__(self, engine_path, time_limit):
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path, timeout=10)
        self.time_limit = time_limit

    def play(self, board):
        play_result = self.engine.play(board, chess.engine.Limit(time=self.time_limit))
        result = {
            'move': play_result.move,
            'resigned': play_result.resigned
        }
        return result

    def close(self):
        self.engine.quit()
