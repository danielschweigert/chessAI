import unittest

from chessAI.model.representation.volume import VolumeRepresentation


class PositionIndexToCoordinateTest(unittest.TestCase):

    def test_position_index_to_coordinate(self):

        correct_mappings = {
            63: (7, 7), 62: (6, 7), 61: (5, 7), 60: (4, 7), 59: (3, 7), 58: (2, 7), 57: (1, 7), 56: (0, 7),
            55: (7, 6), 54: (6, 6), 53: (5, 6), 52: (4, 6), 51: (3, 6), 50: (2, 6), 49: (1, 6), 48: (0, 6),
            47: (7, 5), 46: (6, 5), 45: (5, 5), 44: (4, 5), 43: (3, 5), 42: (2, 5), 41: (1, 5), 40: (0, 5),
            39: (7, 4), 38: (6, 4), 37: (5, 4), 36: (4, 4), 35: (3, 4), 34: (2, 4), 33: (1, 4), 32: (0, 4),
            31: (7, 3), 30: (6, 3), 29: (5, 3), 28: (4, 3), 27: (3, 3), 26: (2, 3), 25: (1, 3), 24: (0, 3),
            23: (7, 2), 22: (6, 2), 21: (5, 2), 20: (4, 2), 19: (3, 2), 18: (2, 2), 17: (1, 2), 16: (0, 2),
            15: (7, 1), 14: (6, 1), 13: (5, 1), 12: (4, 1), 11: (3, 1), 10: (2, 1), 9: (1, 1), 8: (0, 1),
            7: (7, 0), 6: (6, 0), 5: (5, 0), 4: (4, 0), 3: (3, 0), 2: (2, 0), 1: (1, 0), 0: (0, 0),
        }

        for index, x_y in correct_mappings.items():
            self.assertEqual(x_y, VolumeRepresentation.position_index_to_coordinate(index))
