import chess
import numpy as np


class VolumeRepresentation:

    @staticmethod
    def position_index_to_coordinate(chess_position_index):
        """
        For a chess board position index (0-63), returns the respective x, y coordinates.

        (0, 0) :    lower right corner
        (7, 0) :    lower left corner
        (0, 7) :    upper right corner
        (7, 7) :    upper left corner

        Args:
            chess_position_index (int):             integer position index

        Returns:
            int:                                    x position
            int:                                    y position

        """

        x = chess_position_index % 8
        y = chess_position_index // 8
        return x, y

    @staticmethod
    def piece_to_vector(piece):
        """

        Returns 1d vector representation of a piece.

        The first position of the vector represents the side: 0 for starting side; 1 for responding side

        The remaining 6 positions are a 1-hot encoding of the piece type.


        Args:
            piece (chess.Piece):                piece to transform

        Returns:
            numpy.array:                        (1, 7) vector
        """

        piece_str = piece.__str__()
        piece_index = {
            'k': 1,
            'q': 2,
            'r': 3,
            'b': 4,
            'n': 5,
            'p': 6
        }

        _vector = np.zeros(7)
        _vector[0] = 1 if piece_str.islower() else 0
        _vector[piece_index[piece_str.lower()]] = 1

        return _vector

    @staticmethod
    def board_to_volume(board):
        """
        Returns a 3d volume representation of the chess board with the 3rd dimension representing the piece at the
        respective 2d coordinates.

        Args:
            board (chess.Board):                A situation on the chess board

        Returns:
            numpay.array                        (8, 8, 7) array representation

        """
        
        volume = np.zeros(shape=(8, 8, 7))
        piece_map = board.piece_map()

        for position_index, piece in piece_map.items():
            x, y = VolumeRepresentation.position_index_to_coordinate(position_index)
            piece_vector = VolumeRepresentation.piece_to_vector(piece)
            volume[x][y][:] = piece_vector

        return volume
