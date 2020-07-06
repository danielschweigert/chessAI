import unittest
import chess
from chessAI.model.training.campaign.random import RandomWalkTrainingCampaign
from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.util.logging import DataFileLogger
from config import config


class RandomWalkTrainingCampaignTest(unittest.TestCase):

    def test_random_walk_training_campaign(self):

        evaluator = SimpleCNNEvaluator()
        player = ShallowPlayer(evaluator)
        n_parameters = len(evaluator.get_parameters())
        engine_player_path = config['test']['uci_engine_path']
        engine_player_time_limit = 0.1
        data_file_logger = DataFileLogger(config['test']['data_file_logger_path'], n_parameters=n_parameters,
                                          append=True)

        initial_board = chess.Board()
        initial_board.clear_board()
        initial_board.set_piece_at(square=chess.C4, piece=chess.Piece.from_symbol('K'))
        initial_board.set_piece_at(square=chess.F4, piece=chess.Piece.from_symbol('k'))
        initial_board.set_piece_at(square=chess.H4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.G4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.H5, piece=chess.Piece.from_symbol('q'))
        print(initial_board)
        initial_boards = [initial_board]
        kwargs = {
            'n_rounds_series': 10,
            'n_iterations_training': 50,
            'side': 1,
            'random_walk_n_subset': 40,
            'max_abs_rel_change': 0.1,
            'data_loggers': [data_file_logger]
        }
        rwtc = RandomWalkTrainingCampaign(player, engine_player_path, engine_player_time_limit, initial_boards,
                                          **kwargs)
        rwtc.run()
