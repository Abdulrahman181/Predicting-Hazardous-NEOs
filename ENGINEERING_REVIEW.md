# Engineering review — Predicting-Hazardous-NEOs

**Date:** 2026-10-14
**Scope:** all tracked Python/notebook/documentation/dependency files in this checkout
**Repository:** `Abdulrahman181/Predicting-Hazardous-NEOs`

## Executive summary

The original repository contained one output-heavy notebook, one source-URL text file, and a README. It did not contain the CSV used by the notebook, a dependency manifest, tests, or a Python module. The notebook's cells were individually parseable, but it was not reproducible: it used a developer-local Windows path, relied on execution order and stale variables, reported metrics from the wrong prediction variable in places, and included resampling on the complete dataset (a leakage risk).

The notebook is now a small, output-free walkthrough backed by `neos_pipeline.py`. The pipeline validates the real CSV, removes identifier columns, performs a stratified fixed-seed split, and fits imputation/scaling inside model pipelines after the split. It evaluates logistic regression and a class-weighted random forest using accuracy, balanced accuracy, precision, recall, F1, and ROC AUC. No fabricated data or metrics were added.

## Findings in the original checkout

- **Data path:** a developer-local Windows absolute path made execution machine-specific. `NASA_Data.txt` contains only a Kaggle URL, not data.
- **Undefined/order-dependent state:** cells reused `model`, `y_pred`, `AccScore`, `results`, and other variables across multiple models. The random-forest section evaluated a decision-tree prediction in some print statements. A fresh, linear execution was not dependable.
- **Schema fragility:** `X = df.iloc[:, :-1]` assumed the last column was the target instead of checking `is_hazardous` and required features.
- **Leakage risk:** the notebook defined oversampling/undersampling and applied resampling to `X, y` before the train/test split. Any fitted imputation or resampling must be restricted to training data.
- **Preprocessing inconsistency:** logistic regression was trained on scaled arrays but its train/test `.score()` calls used unscaled data. Missing values were filled using medians computed over the full dataset before splitting.
- **Reproducibility:** the split had a seed, but estimators and resampling had inconsistent or absent seeds; class stratification was not requested.
- **Dependency hygiene:** `imblearn` imports were unused in the final model path and were not declared anywhere. Required notebook/runtime packages were also undeclared.
- **Tracked artefacts:** the notebook contained 183 KB of old outputs, including tables, plots, and historical metric text. These could not be treated as current results.
- **Documentation:** the README claimed a best model and results without reproducible values in the checkout and described a repository layout that did not exist.

## Implemented changes

- Added `neos_pipeline.py` with explicit path resolution, schema checks, binary-target normalisation, duplicate removal, and actionable missing-data errors.
- Added two deterministic scikit-learn pipelines. Imputation and scaling are learned after a stratified split; class imbalance uses `class_weight="balanced"` rather than full-dataset resampling.
- Replaced `Project_NEOs.ipynb` with an output-free, two-cell execution path that delegates to the module.
- Added `requirements.txt` for runtime, notebook, and validation dependencies. Unused `imbalanced-learn` was not added.
- Added `.gitignore` so downloaded data and generated artefacts remain local.
- Added `tests/test_engineering.py` for notebook AST/output checks, required-file checks, and the missing-data guard.
- Rewrote `README.md` to state the data/metrics status, setup, schema, methodology safeguards, validation commands, and limitations.
- Added this audit report.

## Validation performed

The following checks were run in the sandbox:

- Parsed every original notebook code cell with Python AST; no cell-level syntax error was found, but Ruff reported 8 import/redefinition findings.
- Ran Ruff after the changes: `ruff check .` passes.
- Ran the repository tests: `pytest -q` passes.
- Parsed the final notebook as JSON and AST-checked each code cell; all code cells have no outputs and `execution_count: null`.
- Inspected Git status and tracked files; only this repository was modified.

A full model training run was **not** claimed: the external CSV is absent from the repository. The installed sandbox happened to provide pandas/scikit-learn, but the declared environment should still be installed from `requirements.txt` for reproducibility. No metric values were generated or copied into this report.

## Remaining scientific/engineering considerations

The source dataset may contain repeated observations of the same object. Before operational or scientific use, assess object-level grouping and temporal drift; a time-aware or grouped holdout may be more appropriate than a random split. Threshold selection, calibration, error analysis, and independent validation remain future work.
