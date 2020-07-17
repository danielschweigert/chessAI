import unittest
import os
import chess
from chessAI.model.training.campaign.random_walk import RandomWalkTrainingCampaign
from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator
from chessAI.model.evaluation.cnn.simpleCNNEvaluation import SimpleCNNEvaluator
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.model.play.factory import PlayerFactory
from chessAI.util.logging import DataFileLogger
from config import config


class RandomWalkTrainingCampaignTest(unittest.TestCase):

    def test_random_walk_training_campaign_cnn(self):

        evaluator = SimpleCNNEvaluator()
        model_player = ShallowPlayer(evaluator)
        n_parameters = len(evaluator.get_parameters())
        engine_player = PlayerFactory.create_player(config['test']['engine_player'])
        data_file_logger = DataFileLogger(config['test']['data_file_logger_path'], append=True)

        initial_board = chess.Board()
        initial_board.clear_board()
        initial_board.set_piece_at(square=chess.C4, piece=chess.Piece.from_symbol('K'))
        initial_board.set_piece_at(square=chess.F4, piece=chess.Piece.from_symbol('k'))
        initial_board.set_piece_at(square=chess.H4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.G4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.H5, piece=chess.Piece.from_symbol('q'))
        initial_board_fens = [initial_board.fen()]

        kwargs = {
            'data_loggers': [data_file_logger]
        }

        rwtc = RandomWalkTrainingCampaign(model_player=model_player,
                                          engine_player=engine_player,
                                          side=1,
                                          n_rounds_series=5,
                                          n_iterations_training=5,
                                          random_walk_n_subset=40,
                                          max_abs_rel_change=0.1,
                                          initial_board_fens=initial_board_fens,
                                          kwargs=kwargs)
        score, parameters = rwtc.run()
        rwtc.engine_player.close()
        self.assertIsInstance(score, float)
        self.assertEqual(n_parameters, len(parameters))

    def test_random_walk_training_campaign_fcn(self):

        evaluator = SimpleFCNEvaluator()
        model_player = ShallowPlayer(evaluator)
        n_parameters = len(evaluator.get_parameters())
        engine_player = PlayerFactory.create_player(config['test']['engine_player'])
        data_file_logger = DataFileLogger(config['test']['data_file_logger_path'], append=True)

        initial_board = chess.Board()
        initial_board.clear_board()
        initial_board.set_piece_at(square=chess.C4, piece=chess.Piece.from_symbol('K'))
        initial_board.set_piece_at(square=chess.F4, piece=chess.Piece.from_symbol('k'))
        initial_board.set_piece_at(square=chess.H4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.G4, piece=chess.Piece.from_symbol('q'))
        initial_board.set_piece_at(square=chess.H5, piece=chess.Piece.from_symbol('q'))
        initial_board_fens = [initial_board.fen()]

        kwargs = {
            'data_loggers': [data_file_logger]
        }
        rwtc = RandomWalkTrainingCampaign(model_player=model_player,
                                          engine_player=engine_player,
                                          side=1,
                                          n_rounds_series=5,
                                          n_iterations_training=5,
                                          random_walk_n_subset=40,
                                          max_abs_rel_change=0.1,
                                          initial_board_fens=initial_board_fens,
                                          kwargs=kwargs)
        score, parameters = rwtc.run()
        rwtc.engine_player.close()
        self.assertIsInstance(score, float)
        self.assertEqual(n_parameters, len(parameters))

    def tearDown(self):
        os.remove(config['test']['data_file_logger_path'])
