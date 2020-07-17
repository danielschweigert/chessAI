import unittest
import chess
import os
from chessAI.model.training.campaign.random_walk import RandomWalkTrainingCampaign
from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator
from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.util.logging import DataFileLogger
from config import config


class RandomWalkTrainingCampaignTest(unittest.TestCase):

    def test_random_walk_training_campaign_cnn(self):

        evaluator = SimpleCNNEvaluator()
        player = ShallowPlayer(evaluator)
        n_parameters = len(evaluator.get_parameters())
        engine_player_path = config['test']['uci_engine_path']
        engine_player_time_limit = 0.1
        data_file_logger = DataFileLogger(config['test']['data_file_logger_path'], append=True)

        initial_board = chess.Board()
        initial_board.clear_board()
        initial_board.set_piece_at(square=chess.C4, piece=chess.Piece.from_symbol('K'))
        initial_board.set_piece_at(square=chess.F4, piece=chess.Piece.from_symbol('k'))
        initial_board.set_piece_at(square=chess.H4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.G4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.H5, piece=chess.Piece.from_symbol('q'))
        initial_boards = [initial_board]
        kwargs = {
            'n_rounds_series': 5,
            'n_iterations_training': 5,
            'side': 1,
            'random_walk_n_subset': 40,
            'max_abs_rel_change': 0.1,
            'data_loggers': [data_file_logger]
        }
        rwtc = RandomWalkTrainingCampaign(player, engine_player_path, engine_player_time_limit, initial_boards,
                                          **kwargs)
        score, parameters = rwtc.run()
        rwtc.engine_player.close()
        self.assertIsInstance(score, float)
        self.assertEqual(n_parameters, len(parameters))

    def test_random_walk_training_campaign_fcn(self):

        evaluator = SimpleFCNEvaluator()
        player = ShallowPlayer(evaluator)
        n_parameters = len(evaluator.get_parameters())
        engine_player_path = config['test']['uci_engine_path']
        engine_player_time_limit = 0.1
        data_file_logger = DataFileLogger(config['test']['data_file_logger_path'], append=True)

        initial_board = chess.Board()
        initial_board.clear_board()
        initial_board.set_piece_at(square=chess.C4, piece=chess.Piece.from_symbol('K'))
        initial_board.set_piece_at(square=chess.F4, piece=chess.Piece.from_symbol('k'))
        initial_board.set_piece_at(square=chess.H4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.G4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.H5, piece=chess.Piece.from_symbol('q'))
        initial_boards = [initial_board]
        kwargs = {
            'n_rounds_series': 5,
            'n_iterations_training': 5,
            'side': 1,
            'random_walk_n_subset': 5000,
            'max_abs_rel_change': 0.1,
            'data_loggers': [data_file_logger]
        }
        rwtc = RandomWalkTrainingCampaign(player, engine_player_path, engine_player_time_limit, initial_boards,
                                          **kwargs)
        score, parameters = rwtc.run()
        rwtc.engine_player.close()
        self.assertIsInstance(score, float)
        self.assertEqual(n_parameters, len(parameters))
