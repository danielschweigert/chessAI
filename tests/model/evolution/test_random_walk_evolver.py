import unittest
import numpy as np
from chessAI.model.evolution.random_walk import RandomWalkEvolver


class RandomWalkEvolverTest(unittest.TestCase):

    def test_random_walk_evolve(self):

        vector_size = 50
        n_subset = 5
        max_abs_rel_change = 0.05
        vector = np.arange(vector_size)
        rwe = RandomWalkEvolver(n_subset, max_abs_rel_change)
        evolved_vector = rwe.evolve(vector)
        delta = sum(np.abs(vector - evolved_vector))
        self.assertGreater(delta, 0)
        n_unchanged = len(np.where(vector - evolved_vector == 0)[0])
        self.assertGreaterEqual(n_unchanged, vector_size-n_subset)
