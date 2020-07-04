class BaseEvaluator:
    """
    An evaluator computes a score of a positional chess situation.
    """

    def evaluate(self, volume_representation):
        raise NotImplementedError()
