import unittest
from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator
from chessAI.util.error import MissingParameterError
from chessAI.model.evaluation.factory import EvaluatorFactory


class EvaluatorFactoryTest(unittest.TestCase):

    def test_missing_class_name(self):

        parameters = {}
        self.assertRaises(MissingParameterError, EvaluatorFactory.create_evaluator, parameters)

    def test_create_SimpleFCNEvaluator(self):

        parameters = {
            'class': 'SimpleFCNEvaluator'
        }

        evaluator = EvaluatorFactory.create_evaluator(parameters)
        self.assertIsInstance(evaluator, SimpleFCNEvaluator)
