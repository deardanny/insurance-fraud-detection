import json
from pathlib import Path
import numpy as np
import pytest
from thresholding import total_cost, select_cost_threshold


def test_asymmetric_cost_changes_the_decision():
    labels, probabilities, grid = [1, 0, 0], [.4, .6, .1], [.3, .5, .7]
    chosen, costs = select_cost_threshold(labels, probabilities, grid, 15000, 500)
    assert chosen == .3
    np.testing.assert_array_equal(costs, [500, 15500, 15000])


def test_boundary_is_inclusive():
    assert total_cost(.5, [1, 0], [.5, .5], 15, 2) == 2


@pytest.mark.parametrize('labels,probs', [([1], []), ([2], [.5]), ([1], [np.nan]), ([0], [1.1])])
def test_rejects_invalid_inputs(labels, probs):
    with pytest.raises(ValueError):
        total_cost(.5, labels, probs)


def test_cost_selection_cell_does_not_use_test_labels():
    notebook = json.loads((Path(__file__).resolve().parents[1] / 'notebooks/fraud_analysis.ipynb').read_text())
    source = '\n'.join(''.join(c['source']) for c in notebook['cells'] if c['cell_type'] == 'code')
    import ast
    calls = [n for n in ast.walk(ast.parse(source)) if isinstance(n, ast.Call)
             and isinstance(n.func, ast.Name) and n.func.id == 'select_cost_threshold']
    assert len(calls) == 1
    assert [n.id for n in calls[0].args[:2]] == ['y_train', 'y_prob_xgb_oof']
