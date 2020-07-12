from ..base import BaseEvaluator
import torch.nn as nn


class SimpleFCNEvaluator(BaseEvaluator):
    """
    Uses a FCN on a volume representation of a chess board situation to compute an evaluation score.
    """

    def __init__(self):
        super(SimpleFCNEvaluator, self).__init__()
        self.fc_1 = nn.Linear(8 * 8 * 7, 450)
        self.relu_1 = nn.ReLU()
        self.fc_2 = nn.Linear(450, 50)
        self.relu_2 = nn.ReLU()
        self.fc_3 = nn.Linear(50, 1)

    def evaluate(self, volume_representation):
        """
        Args:
            volume_representation (VolumeRepresentation):           board situation

        Returns:
            float:                                                  situation score
        """

        x = volume_representation.get_tensor()
        x = x.view(x.size(0), -1)
        x = self.fc_1(x)
        x = self.relu_1(x)
        x = self.fc_2(x)
        x = self.relu_2(x)
        x = self.fc_3(x)

        score = x.data[0][0].item()
        return score
