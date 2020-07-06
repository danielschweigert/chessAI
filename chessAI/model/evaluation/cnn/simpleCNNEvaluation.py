from ..base import BaseEvaluator
import torch.nn as nn


class SimpleCNNEvaluator(BaseEvaluator):
    """
    Uses a CNN on a volume representation of a chess board situation to compute an evaluation score.
    """

    def __init__(self):
        super(SimpleCNNEvaluator, self).__init__()
        self.conv_1 = self._conv_layer_set(1, 2)
        self.fc_1 = nn.Linear(54, 1)
        self.relu_1 = nn.LeakyReLU()

    def _conv_layer_set(self, in_c, out_c):
        conv_layer = nn.Sequential(
            nn.Conv3d(in_c, out_c, kernel_size=(2, 2, 2), padding=0),
            nn.LeakyReLU(),
            nn.MaxPool3d((2, 2, 2))
        )
        return conv_layer

    def evaluate(self, volume_representation):
        """
        Args:
            volume_representation (VolumeRepresentation):           board situation

        Returns:
            float:                                                  situation score
        """

        x = volume_representation.get_tensor()
        x = self.conv_1(x)
        x = x.view(x.size(0), -1)
        x = self.fc_1(x)
        x = self.relu_1(x)
        score = x.data[0][0].item()
        return score
