# Validation scope

## Passed checks

- Parsed the notebook JSON, validated its nbformat schema, and parsed all 68 code cells plus the plotting script as Python.
- Executed all 68 notebook code cells in order with an isolated namespace and fresh variables, using the opt-in reduced smoke mode: 1,200 training and 800 test encounters, three CV folds, one model candidate per family, one feature-selection threshold, two permutation repeats, and five bootstrap resamples. Training, prediction, scoring, feature interpretation, feature selection, bootstrap, and plotting completed without an exception.
- Executed the default full-data preparation path without fitting classifiers: 25,441 training and 25,442 test encounters, 43 predictors after removal/grouping, 139 encoded predictors, and the same six removed columns as the recorded analysis.
- Confirmed 3,924 shared patient identifiers across the preserved outer split; dataset row counts, binary label counts, and distinct-patient counts were checked against the local CSV.
- Regenerated summary charts and visually inspected all packaged figures.
- Checked local Markdown links, excluded private/administrative references, verified that the source notebook and inputs stayed unchanged, and checked archive integrity.

The smoke check ran in a non-interactive harness with rich display suppressed and figures closed after rendering; it was not a browser/Jupyter UI test. The distributed notebook deliberately starts with cleared outputs and execution counters so smoke metrics cannot be mistaken for historical scores.

## Environment and limits

Checks used Python 3.12.0, NumPy 2.5.4, pandas 3.1.0, scikit-learn 1.9.1, and Matplotlib 3.11.2 from existing temporary validation dependencies. These versions are not a historical experiment lock. The supplied dependency file specifies compatible major-version ranges; a fresh installation of the complete Jupyter environment was not performed.

The full-data classifier grid searches, original 100-resample bootstrap, and full permutation-importance computation were not rerun. Historical results remain recorded outputs, not newly verified model performance. Patient-disjoint, temporal, prospective, calibration, and subgroup evaluations were not performed.
