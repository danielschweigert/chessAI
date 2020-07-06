class Player:
    """
    A player evaluates and returns a best choice for a move based on its underlying selection logic.
    """

    def get_highest_ranked_move(self, board, side=0):
        raise NotImplementedError()

    def close(self):
        pass

    def play(self, board, **kwargs):
        side = kwargs['side']
        highest_ranked_move, _ = self.get_highest_ranked_move(board, side)
        result = {
            'move': highest_ranked_move,
            'resigned': False
        }
        return result
