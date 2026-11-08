# Publication validation — 2026-11-08

- Python 3.12, pinned direct dependencies, macOS OpenMP runtime.
- `python -m pytest -q`: **7 passed**, covering asymmetric cost decisions, threshold boundaries, invalid input and use of training-only threshold selection in the notebook.
- `FRAUD_DATA_PATH=/path/to/carclaims.csv python run_analysis.py`: **all 53 code cells completed without errors**, including all six models and aggregate exports. Kernel execution took about 83 seconds in the local environment; this is not a performance benchmark.
- Local course input: 15,420 rows; stratified split with 3,084 test rows. The input CSV is not distributed.
- Publication-run aggregate results are in `results/`; figures in `docs/` are extracted from the actual corrected run.
- Raw row previews, original stored notebook outputs, personal Drive paths and unrelated files are excluded.
- Historical academic results may differ because threshold-selection leakage and runtime compatibility were corrected. The data was previously explored; this is not external validation.
- The fitted model comparison, tests and notebook run do not validate real-world insurance costs, fairness or deployment readiness.
