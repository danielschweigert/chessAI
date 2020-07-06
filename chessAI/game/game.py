class Game:

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
            reason = 'resignation'

        if self.board.is_checkmate():
            game_over = True
            score = int(current_player == self.player_1)
            reason = 'checkmate'

        if self.board.is_stalemate():
            game_over = True
            score = 0.5
            reason = 'stalemate'

        if self.board.is_insufficient_material():
            game_over = True
            score = 0.5
            reason = 'insufficient material'

        if self.board.can_claim_threefold_repetition():
            game_over = True
            score = 0.5
            reason = '3-fold repetition'

        if self.board.can_claim_fifty_moves():
            game_over = True
            score = 0.5
            reason = '50 moves rule'

        return game_over, score, reason

    def run(self):

        player_to_move = self.player_1
        score = None
        reason = None

        n_half_moves = 0
        while True:

            play_result = player_to_move.play(self.board)
            move = play_result['move']
            print(move)
            self.board.push(move)
            print(self.board)

            game_over, score, reason = self.is_game_over(current_player=player_to_move, play_result=play_result)

            if game_over:
                break

            player_to_move = self.player_2 if player_to_move == self.player_1 else self.player_1

            n_half_moves += 1

        self.player_1.close()
        self.player_2.close()

        game_result = {
            'score': score,
            'reason': reason,
            'nth_move': (n_half_moves + 1) // 2
        }
        return game_result
