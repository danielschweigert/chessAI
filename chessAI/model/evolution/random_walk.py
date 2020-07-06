import numpy as np


class RandomWalkEvolver:

    def __init__(self, n_subset, max_abs_rel_change):
        self.n_subset = n_subset
        self.max_abs_rel_change = max_abs_rel_change

    def evolve(self, vector):
        n_subset = self.n_subset if self.n_subset <= vector.shape[0] else vector.shape[0]
        indices_to_change = np.random.choice(a=np.arange(vector.shape[0]), size=n_subset, replace=False)
        rel_change = np.zeros(vector.shape[0])
        rel_change[indices_to_change] = self.max_abs_rel_change * (np.random.uniform(size=n_subset) - 0.5)
        return vector + rel_change
