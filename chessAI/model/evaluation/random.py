import random
from .base import BaseEvaluator


class RandomEvaluator(BaseEvaluator):
    """
    Gives a campaign score regardless of the situation on the board.
    """

    def evaluate(self, volume_representation):
        """
        Args:
            volume_representation (VolumeRepresentation):           board situation

        Returns:
            float:                                                  situation score
        """

        score = random.randrange(-100, 100)

        return score


