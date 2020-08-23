import os
from chessAI.util.error import MissingParameterError


class DataLogger:

    def log(self, score, parameters):
        raise NotImplementedError()

    @staticmethod
    def create_data_logger(parameters):
        data_loggers = list()
        for logger_params in parameters:
            class_name = logger_params['class']

            if class_name == DataFileLogger.__name__:

                if 'data_file_path' not in logger_params:
                    raise MissingParameterError('data_file_path')

                data_file_path = logger_params['data_file_path']

                append = logger_params.get('append', None)
                if append is None:
                    dl = DataFileLogger(data_file_path)
                else:
                    dl = DataFileLogger(data_file_path, append)
                data_loggers.append(dl)

        return data_loggers


class DataFileLogger(DataLogger):

    def __init__(self, data_file_path, append=True):
        super(DataFileLogger, self).__init__()
        self.header_written = False
        self.data_file_path = data_file_path
        if append:
            if os.path.exists(data_file_path):
                with open(data_file_path, 'r') as f:
                    i = 0
                    _ = f.readline()
                    line = f.readline()
                    while line != '':
                        i += 1
                        line = f.readline()
                    self.index = i
                    self.header_written = True
                return
            else:
                f = open(data_file_path, 'a')
        else:
            f = open(data_file_path, 'w')
        f.close()
        self.index = 0

    def write_header(self, parameters):
        """
        Writes a header line based on the number of parameters that are being written.

        Args:
            parameters (list):                  list of parameter values
        """
        n_parameters = len(parameters)
        parameter_header = ','.join([f'parameter_{p}' for p in range(n_parameters)])
        header = f'index,score,{parameter_header},\n'
        with open(self.data_file_path, 'a') as f:
            f.write(header)
        self.header_written = True

    def log(self, score, parameters):

        if not self.header_written:
            self.write_header(parameters)

        parameter_line = ','.join([str(p) for p in parameters])
        line = f'{self.index},{score},{parameter_line},\n'

        with open(self.data_file_path, 'a') as f:
            f.write(line)

        self.index += 1
