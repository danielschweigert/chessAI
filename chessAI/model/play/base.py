class Player:
    """
    A player evaluates and returns a best choice for a move based on its underlying selection logic.
    """

    def get_highest_ranked_move(self, board, side=0):
        raise NotImplementedError()
