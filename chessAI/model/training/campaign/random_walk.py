from chessAI.game.game import Series
from chessAI.model.evolution.random_walk import RandomWalkEvolver
from chessAI.model.play.engine import EnginePlayer
from chessAI.model.play.factory import PlayerFactory
from chessAI.util.logging import DataLogger


class RandomWalkTrainingCampaign:

    def __init__(self,
                 model_player,
                 engine_player,
                 side,
                 n_rounds_series,
                 n_iterations_training,
                 random_walk_n_subset,
                 max_abs_rel_change,
                 initial_boards,
                 kwargs
                 ):

        self.model_player = model_player
        self.engine_player = engine_player
        self.initial_boards = initial_boards
        self.n_rounds_series = n_rounds_series
        self.n_iterations_training = n_iterations_training
        self.side = side
        random_walk_n_subset = random_walk_n_subset
        random_walk_max_abs_rel_change = max_abs_rel_change
        self.random_walk_evolver = RandomWalkEvolver(n_subset=random_walk_n_subset,
                                                     max_abs_rel_change=random_walk_max_abs_rel_change)
        self.data_loggers = kwargs.get('data_loggers', [])

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
            series_result = series.run()
            score = series_result['scores'][player_name]['total']

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

    @classmethod
    def from_schedule(cls, schedule):

        player_parameters = schedule['player']
        model_player = PlayerFactory.create_player(player_parameters)

        engine_parameters = schedule['engine_player']
        engine_player = PlayerFactory.create_player(engine_parameters)

        side = schedule['side']
        n_rounds_series = schedule['n_rounds_series']
        n_iterations_training = schedule['n_iterations_training']
        random_walk_n_subset = schedule['random_walk_n_subset']
        max_abs_rel_change = schedule['max_abs_rel_change']
        initial_boards = schedule['initial_boards']

        data_logger_params = schedule['logger']
        data_loggers = DataLogger.create_data_logger(data_logger_params)

        rwtc = cls(model_player=model_player,
                   engine_player=engine_player,
                   side=side,
                   n_rounds_series=n_rounds_series,
                   n_iterations_training=n_iterations_training,
                   random_walk_n_subset=random_walk_n_subset,
                   max_abs_rel_change=max_abs_rel_change,
                   initial_boards=initial_boards,
                   kwargs={'data_loggers': data_loggers}
                   )

        return rwtc
