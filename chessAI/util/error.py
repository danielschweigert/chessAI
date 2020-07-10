class MissingParameterError(Exception):

    def __init__(self, parameter_name):
        super().__init__()
        self.parameter_name = parameter_name
        self.message = f'Missing parameter: {parameter_name}'
