import copy


class Reason:
    """
    Reasons how games end.
    """
    RESIGNATION = 'resignation'
    CHECKMATE = 'checkmate'
    STALEMATE = 'stalemate'
    INSUFFICIENT_MATERIAL = 'insufficient material'
    THREE_FOLD_REPETITION = '3-fold repetition'
    FIFTY_MOVES_ROLE = '50 moves rule'


class Game:
    """
    Sets up and conducts a full game between 2 players and reports the result.
    """

    def __init__(self, player_1, player_2, initial_board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = initial_board

    def is_game_over(self, current_player, play_result):
        game_over = False
        score = None
        reason = None

        if play_result['resigned']:
            game_over = True
            score = int(current_player == self.player_2)
            reason = Reason.RESIGNATION

        if self.board.is_checkmate():
            game_over = True
            score = int(current_player == self.player_1)
            reason = Reason.CHECKMATE

        if self.board.is_stalemate():
            game_over = True
            score = 0.5
            reason = Reason.STALEMATE

        if self.board.is_insufficient_material():
            game_over = True
            score = 0.5
            reason = Reason.INSUFFICIENT_MATERIAL

        if self.board.can_claim_threefold_repetition():
            game_over = True
            score = 0.5
            reason = Reason.THREE_FOLD_REPETITION

        if self.board.can_claim_fifty_moves():
            game_over = True
            score = 0.5
            reason = Reason.FIFTY_MOVES_ROLE

        return game_over, score, reason

    def run(self):

        player_to_move = self.player_1
        score = None
        reason = None

        n_half_moves = 0
        while True:

            side = int(not self.board.turn)
            play_result = player_to_move.play(self.board, side=side)
            move = play_result['move']
            self.board.push(move)

            game_over, score, reason = self.is_game_over(current_player=player_to_move, play_result=play_result)

            if game_over:
                break

            player_to_move = self.player_2 if player_to_move == self.player_1 else self.player_1

            n_half_moves += 1

        game_result = {
            'score': score,
            'reason': reason,
            'nth_move': (n_half_moves + 1) // 2
        }
        return game_result


class Series:
    """
    Sets up and executes a series of games of n_rounds for each of the boards in initial_boards and reports the results.
    """

    def __init__(self, player_1, player_2, initial_boards, n_rounds=100):
        self.player_1 = player_1
        self.player_2 = player_2
        self.initial_boards = initial_boards
        self.n_rounds = n_rounds

    def run(self):

        result = {
            'rounds_completed': 0,
            'scores': {
                'player_1': {
                    'total': 0,
                    'n_wins': 0,
                    'n_draws': 0,
                },
                'player_2': {
                    'total': 0,
                    'n_wins': 0,
                    'n_draws': 0,
                }
            },
            'reasons': {
                Reason.RESIGNATION: 0,
                Reason.CHECKMATE: 0,
                Reason.FIFTY_MOVES_ROLE: 0,
                Reason.THREE_FOLD_REPETITION: 0,
                Reason.INSUFFICIENT_MATERIAL: 0,
                Reason.STALEMATE: 0
            }
        }

        for initial_board in self.initial_boards:
            for i in range(self.n_rounds):

                _board = copy.deepcopy(initial_board)

                game = Game(player_1=self.player_1,
                            player_2=self.player_2,
                            initial_board=_board)

                game_result = game.run()

                result['rounds_completed'] += 1
                if game_result['score'] == 1:
                    result['scores']['player_1']['n_wins'] += 1
                    result['scores']['player_1']['total'] += 1
                    result['scores']['player_2']['total'] -= 1
                if game_result['score'] == 0.5:
                    result['scores']['player_1']['n_draws'] += 1
                    result['scores']['player_2']['n_draws'] += 1
                    result['scores']['player_1']['total'] += 0.5
                    result['scores']['player_2']['total'] += 0.5
                if game_result['score'] == 0:
                    result['scores']['player_2']['n_wins'] += 1
                    result['scores']['player_1']['total'] -= 1
                    result['scores']['player_2']['total'] += 1
                result['reasons'][game_result['reason']] += 1

        return result
