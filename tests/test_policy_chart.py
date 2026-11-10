"""Validate the policy chart against an intentionally imbalanced toy cohort."""
import json
from pathlib import Path
from unittest.mock import patch

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest


def test_policy_reference_line_uses_claim_weighted_overall_rate():
    # Ten claims: the two policy rates are 12.5% and 50%, overall rate is 20%.
    frame = pd.DataFrame({'PolicyType': ['Demo A'] * 8 + ['Demo B'] * 2,
                          'FraudFound': [1] + [0] * 7 + [1, 0]})
    notebook = json.loads((Path(__file__).resolve().parents[1] / 'notebooks/fraud_analysis.ipynb').read_text())
    source = next(''.join(c['source']) for c in notebook['cells']
                  if c['cell_type'] == 'code' and ''.join(c['source']).startswith('policy_fraud ='))
    context = {'df': frame, 'plt': plt}
    try:
        with patch.object(plt, 'show'):
            exec(compile(source, 'policy-chart-cell', 'exec'), context)
        ax = context['ax']
        line = next(line for line in ax.lines if line.get_label() == 'Overall average')
        np.testing.assert_allclose(line.get_xdata(), [20.0, 20.0])
        assert sorted(bar.get_width() for bar in ax.patches) == pytest.approx([12.5, 50.0])
    finally:
        plt.close('all')
