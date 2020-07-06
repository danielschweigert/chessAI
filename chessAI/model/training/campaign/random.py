from chessAI.game.game import Series
from chessAI.model.evolution.random_walk import RandomWalkEvolver
from chessAI.game.engine import EnginePlayer


class RandomWalkTrainingCampaign:

    def __init__(self, player, engine_player_path, engine_player_time_limit, initial_boards, **kwargs):

        self.player = player
        self.engine_player = EnginePlayer(engine_path=engine_player_path, time_limit=engine_player_time_limit)
        self.initial_boards = initial_boards
        self.n_rounds_series = kwargs.get('n_rounds_series', 100)
        self.n_iterations_training = kwargs.get('n_iterations_training', 50)
        self.side = kwargs.get('side', 0)
        self.data_loggers = kwargs.get('data_loggers', [])

        random_walk_n_subset = kwargs.get('random_walk_n_subset', 1)
        random_walk_max_abs_rel_change = kwargs.get('max_abs_rel_change', 0.05)
        self.random_walk_evolver = RandomWalkEvolver(n_subset=random_walk_n_subset,
                                                     max_abs_rel_change=random_walk_max_abs_rel_change)

    def _new_series(self, player, engine_player, side, initial_boards, n_rounds_series):
        if side == 0:
            player_1 = player
            player_2 = engine_player
            player_name = 'player_1'
        else:
            player_1 = engine_player
            player_2 = self.player
            player_name = 'player_2'

        series = Series(player_1=player_1,
                        player_2=player_2,
                        initial_boards=initial_boards,
                        n_rounds=n_rounds_series)
        return series, player_name

    def run(self):

        previous_score = None
        previous_params = self.player.evaluator.get_parameters()

        highest_score = None
        best_params = None

        series, player_name = self._new_series(player=self.player,
                                               engine_player=self.engine_player,
                                               side=self.side,
                                               initial_boards=self.initial_boards,
                                               n_rounds_series=self.n_rounds_series)

        for i in range(self.n_iterations_training):
            print(i)
            series_result = series.run()
            score = series_result['scores'][player_name]['total']

            print(i, score, self.player.evaluator.get_parameters())
            for data_loger in self.data_loggers:
                data_loger.log(score, self.player.evaluator.get_parameters())

            if highest_score is None or score > highest_score:
                highest_score = score
                best_params = self.player.evaluator.get_parameters()

            if previous_score is not None and score < previous_score:
                self.player.evaluator.set_parameters(previous_params)

            previous_score = score
            previous_params = self.player.evaluator.get_parameters()

            new_params = self.random_walk_evolver.evolve(self.player.evaluator.get_parameters())
            self.player.evaluator.set_parameters(new_params)
            series, player_name = self._new_series(self.player,
                                                   self.engine_player,
                                                   self.side,
                                                   self.initial_boards,
                                                   self.n_rounds_series)

        return highest_score, best_params
