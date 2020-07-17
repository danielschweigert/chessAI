import unittest
import os
import yaml

from tests import TEST_PATH
from chessAI.model.training.campaign.factory import CampaignFactory
from chessAI.model.training.campaign.random_walk import RandomWalkTrainingCampaign
from chessAI.model.play.shallow import ShallowPlayer
from chessAI.model.play.engine import RandomPlayer
from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator
from chessAI.util.logging import DataFileLogger


class CampaignFactoryTest(unittest.TestCase):

    schedule_file_path = os.path.join(TEST_PATH, 'test_files', 'training_campaign_1.yaml')

    def test_random_walk_training_campaign_creation(self):

        rwtc = CampaignFactory.create_campaign_from_schedule_file(self.schedule_file_path)
        self.assertIsInstance(rwtc, RandomWalkTrainingCampaign)
        self.assertIsInstance(rwtc.model_player, ShallowPlayer)
        self.assertIsInstance(rwtc.model_player.evaluator, SimpleFCNEvaluator)
        self.assertIsInstance(rwtc.engine_player, RandomPlayer)
        self.assertEqual(500, rwtc.random_walk_evolver.n_subset)
        self.assertEqual(0.1, rwtc.random_walk_evolver.max_abs_rel_change)
        self.assertEqual(5, rwtc.n_rounds_series)
        self.assertEqual(50, rwtc.n_iterations_training)
        self.assertEqual(0, rwtc.side)
        self.assertIsInstance(rwtc.data_loggers[0], DataFileLogger)

    def tearDown(self):
        with open(self.schedule_file_path) as f:
            schedule = yaml.safe_load(f.read())
        for _logger in schedule['logger']:
            if 'data_file_path' in _logger:
                os.remove(_logger['data_file_path'])
