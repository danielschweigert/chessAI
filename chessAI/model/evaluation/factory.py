from chessAI.model.evaluation.fcn.simpleFCNEvaluation import SimpleFCNEvaluator
from chessAI.util.error import MissingParameterError


class EvaluatorFactory:

    @staticmethod
    def create_evaluator(parameters):

        if 'class' not in parameters:
            raise MissingParameterError(parameter_name='class')

        evaluator_class_name = parameters['class']

        if evaluator_class_name == SimpleFCNEvaluator.__name__:
            evaluator = SimpleFCNEvaluator()
            return evaluator
