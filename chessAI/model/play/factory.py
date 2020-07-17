from chessAI.model.play.shallow import ShallowPlayer
from chessAI.model.play.engine import RandomPlayer, EnginePlayer
from chessAI.util.error import MissingParameterError
from chessAI.model.evaluation.factory import EvaluatorFactory


class PlayerFactory:

    @staticmethod
    def create_player(parameters):

        if 'class' not in parameters:
            raise MissingParameterError('class')

        player_class_name = parameters['class']

        if player_class_name == RandomPlayer.__name__:

            rp = RandomPlayer()
            return rp

        if player_class_name == EnginePlayer.__name__:

            engine_path = parameters['engine_path']

            # random player if no path to engine provided
            if engine_path == '':
                rp = RandomPlayer()
                return rp

            time_limit = parameters['time_limit']
            ep = EnginePlayer(engine_path, time_limit)
            return ep

        if player_class_name == ShallowPlayer.__name__:

            if 'evaluator' not in parameters:
                raise MissingParameterError('evaluator')

            evaluator_parameters = parameters['evaluator']
            evaluator = EvaluatorFactory.create_evaluator(evaluator_parameters)
            sp = ShallowPlayer(evaluator)
            return sp
