import torch
import torch.nn as nn
from torch.nn.utils import parameters_to_vector, vector_to_parameters


class BaseEvaluator(nn.Module):
    """
    An evaluator computes a score of a positional chess situation.
    """

    def __init__(self):
        super(BaseEvaluator, self).__init__()

    def evaluate(self, volume_representation):
        raise NotImplementedError()

    def get_parameters(self):
        vec = parameters_to_vector(self.parameters())
        vec = vec.detach().numpy()
        return vec

    def set_parameters(self, vec):
        vec = torch.tensor(vec, dtype=torch.float32)
        vector_to_parameters(vec, self.parameters())
