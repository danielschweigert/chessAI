"""
Factory for Logger classes.
"""

from chessAI.util.error import MissingParameterError
from chessAI.util.logging.data import DataFileLogger


class LoggerFactory:

    @staticmethod
    def create_evaluator(parameters):

        if 'class' not in parameters:
            raise MissingParameterError(parameter_name='class')

        logger_class_name = parameters['class']

        if logger_class_name == DataFileLogger.__name__:

            data_file_path = parameters.get('data_file_path', 'log_data.csv')
            append = parameters.get('append', True)

            data_file_logger = DataFileLogger(
                data_file_path=data_file_path,
                append=append
            )

            return data_file_logger
