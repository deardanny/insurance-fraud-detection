"""Cost-based decision thresholds for binary classification experiments."""
import numpy as np


def total_cost(threshold, y_true, y_prob, c_miss=15000, c_fp=500):
    """Modeled FN/FP cost, not a realized financial saving."""
    y = np.asarray(y_true)
    p = np.asarray(y_prob, dtype=float)
    if y.ndim != 1 or p.ndim != 1 or len(y) != len(p) or not len(y):
        raise ValueError("Labels and probabilities must be nonempty aligned vectors")
    if not np.isin(y, [0, 1]).all() or not np.isfinite(p).all() or ((p < 0) | (p > 1)).any():
        raise ValueError("Use binary labels and finite probabilities between zero and one")
    if not np.isfinite([threshold, c_miss, c_fp]).all() or not 0 <= threshold <= 1 or min(c_miss, c_fp) < 0:
        raise ValueError("Invalid threshold or costs")
    prediction = p >= threshold
    return float(np.sum((y == 1) & ~prediction) * c_miss + np.sum((y == 0) & prediction) * c_fp)


def select_cost_threshold(y_train, oof_probabilities, grid, c_miss=15000, c_fp=500):
    """Choose on training OOF predictions. Never pass held-out test labels here."""
    grid = np.asarray(grid, dtype=float)
    if grid.ndim != 1 or not len(grid):
        raise ValueError("Provide a nonempty one-dimensional threshold grid")
    costs = np.array([total_cost(t, y_train, oof_probabilities, c_miss, c_fp) for t in grid])
    return float(grid[np.argmin(costs)]), costs
