from chessAI.model.play.shallow import ShallowPlayer
from chessAI.util.error import MissingParameterError
from chessAI.model.evaluation.factory import EvaluatorFactory


class PlayerFactory:

    @staticmethod
    def create_player(parameters):

        if 'class' not in parameters:
            raise MissingParameterError('class')

        player_class_name = parameters['class']

        if player_class_name == ShallowPlayer.__name__:

            if 'evaluator' not in parameters:
                raise MissingParameterError('evaluator')

            evaluator_parameters = parameters['evaluator']
            evaluator = EvaluatorFactory.create_evaluator(evaluator_parameters)
            sp = ShallowPlayer(evaluator)
            return sp
