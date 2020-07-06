import os


class DataLogger:

    def log(self, score, parameters):
        raise NotImplementedError()


class DataFileLogger(DataLogger):

    def __init__(self, data_file_path, n_parameters, append=True):
        super(DataFileLogger, self).__init__()
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
                return
            else:
                f = open(data_file_path, 'a')
        else:
            f = open(data_file_path, 'w')
        parameter_header = ','.join([f'parameter_{p}' for p in range(n_parameters)])
        header = f'index,score,{parameter_header},\n'
        f.write(header)
        f.close()
        self.index = 0

    def log(self, score, parameters):

        parameter_line = ','.join([str(p) for p in parameters])
        line = f'{self.index},{score},{parameter_line},\n'

        with open(self.data_file_path, 'a') as f:
            f.write(line)

        self.index += 1
