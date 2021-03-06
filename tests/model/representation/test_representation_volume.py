import unittest
import numpy as np
import chess

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

    def test_piece_to_vector(self):

        correct_mappings = {
            chess.Piece.from_symbol('k'): np.array([1, 1, 0, 0, 0, 0, 0]),
            chess.Piece.from_symbol('q'): np.array([1, 0, 1, 0, 0, 0, 0]),
            chess.Piece.from_symbol('r'): np.array([1, 0, 0, 1, 0, 0, 0]),
            chess.Piece.from_symbol('b'): np.array([1, 0, 0, 0, 1, 0, 0]),
            chess.Piece.from_symbol('n'): np.array([1, 0, 0, 0, 0, 1, 0]),
            chess.Piece.from_symbol('p'): np.array([1, 0, 0, 0, 0, 0, 1]),
            chess.Piece.from_symbol('K'): np.array([0, 1, 0, 0, 0, 0, 0]),
            chess.Piece.from_symbol('Q'): np.array([0, 0, 1, 0, 0, 0, 0]),
            chess.Piece.from_symbol('R'): np.array([0, 0, 0, 1, 0, 0, 0]),
            chess.Piece.from_symbol('B'): np.array([0, 0, 0, 0, 1, 0, 0]),
            chess.Piece.from_symbol('N'): np.array([0, 0, 0, 0, 0, 1, 0]),
            chess.Piece.from_symbol('P'): np.array([0, 0, 0, 0, 0, 0, 1]),
        }

        for piece, vector in correct_mappings.items():
            self.assertEqual(list(vector), list(VolumeRepresentation.piece_to_vector(piece)))

    def test_board_to_volume(self):

        correct_mappings = list()

        volume_1 = np.zeros(shape=(8, 8, 7))
        board_1 = chess.Board()
        board_1.clear_board()
        correct_mappings.append((board_1, volume_1))

        volume_2 = np.zeros(shape=(8, 8, 7))
        board_2 = chess.Board()
        board_2.clear_board()
        board_2.set_piece_at(square=59, piece=chess.Piece.from_symbol('k'))
        volume_2[3][7] = [1, 1, 0, 0, 0, 0, 0]
        board_2.set_piece_at(square=3, piece=chess.Piece.from_symbol('K'))
        volume_2[3][0] = [0, 1, 0, 0, 0, 0, 0]
        correct_mappings.append((board_2, volume_2))

        volume_3 = np.zeros(shape=(8, 8, 7))
        board_3 = chess.Board()
        volume_3[7][7] = [1, 0, 0, 1, 0, 0, 0]
        volume_3[6][7] = [1, 0, 0, 0, 0, 1, 0]
        volume_3[5][7] = [1, 0, 0, 0, 1, 0, 0]
        volume_3[4][7] = [1, 1, 0, 0, 0, 0, 0]
        volume_3[3][7] = [1, 0, 1, 0, 0, 0, 0]
        volume_3[2][7] = [1, 0, 0, 0, 1, 0, 0]
        volume_3[1][7] = [1, 0, 0, 0, 0, 1, 0]
        volume_3[0][7] = [1, 0, 0, 1, 0, 0, 0]
        volume_3[7][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[6][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[5][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[4][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[3][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[2][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[1][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[0][6] = [1, 0, 0, 0, 0, 0, 1]
        volume_3[7][0] = [0, 0, 0, 1, 0, 0, 0]
        volume_3[6][0] = [0, 0, 0, 0, 0, 1, 0]
        volume_3[5][0] = [0, 0, 0, 0, 1, 0, 0]
        volume_3[4][0] = [0, 1, 0, 0, 0, 0, 0]
        volume_3[3][0] = [0, 0, 1, 0, 0, 0, 0]
        volume_3[2][0] = [0, 0, 0, 0, 1, 0, 0]
        volume_3[1][0] = [0, 0, 0, 0, 0, 1, 0]
        volume_3[0][0] = [0, 0, 0, 1, 0, 0, 0]
        volume_3[7][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[6][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[5][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[4][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[3][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[2][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[1][1] = [0, 0, 0, 0, 0, 0, 1]
        volume_3[0][1] = [0, 0, 0, 0, 0, 0, 1]

        correct_mappings.append((board_3, volume_3))

        for board, volume in correct_mappings:
            v = VolumeRepresentation.board_to_volume(board)
            self.assertEqual(v.shape, (8, 8, 7))
            for i in range(v.shape[0]):
                for j in range(v.shape[1]):
                    for k in range(v.shape[2]):
                        self.assertEqual(volume[i][j][k], v[i][j][k])
