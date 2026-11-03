# Evaluation and interpretation

## Target and sampling

The binary target combines both recorded readmission intervals. It does not isolate early readmission. The full CSV contains 101,766 encounters, 54,864 with no recorded readmission and 46,902 with a recorded readmission. These proportions describe this encounter dataset, not a population prevalence estimate.

Two stratified `train_test_split` calls with seed 42 first retain half the encounters, then split them evenly: 25,441 training and 25,442 test encounters. No group constraints are imposed. The preserved split has 3,924 patient identifiers shared between outer training and test sets, verified against the included CSV. Repeated patient identifiers can cross the outer split and inner folds. Patient-disjoint or time-based evaluation would be a new experiment and could change scores.

## Preprocessing boundaries

Question marks become missing values after splitting. Identifiers and columns exceeding 40% missingness are removed based on the outer training set. In the recorded run, these removed columns were `encounter_id`, `patient_nbr`, `weight`, `max_glu_serum`, `A1Cresult`, and `medical_specialty`. pandas' default NA parsing treats the literal token `None` in some lab-result fields as missing; this behaviour is preserved and is a modelling choice to revisit rather than proof that every such token represents unknown data.

Diagnosis grouping is deterministic, using simplified code ranges. Missing values become `other` in the preserved implementation because `float('nan')` fails all interval comparisons; the exception-only `unknown` branch is not reached. The grouping is not a complete diagnosis ontology. Numeric admission/discharge/source IDs retain numeric treatment.

Imputation, scaling, one-hot encoding, and model fitting are placed in a scikit-learn pipeline within CV. Column removal and feature-list selection occur before CV. Therefore the full procedure should not be described as entirely free of fold-level preprocessing leakage. Independent cloned preprocessors prevent fitted state from being shared between retained model pipelines.

## Search and feature selection

Three shuffled stratified folds with seed 42 select by F1. Linear SVM uses `SVC(kernel='linear')`, not `LinearSVC`; candidates are C=0.1 and 1. Logistic regression searches six C values from 0.001 to 100 with liblinear. Random forest uses 100 trees and searches depths 2, 4, 6, 8, 10, and 12, with minimum split size 2.

The feature-selection analysis intentionally uses random forest for both the selector and final classifier. It inherits the best random forest parameters and tunes thresholds 0.001, 0.002, 0.005, median, and mean. It does not dynamically switch to another model family if a later rerun ranks another classifier first. F1-based selection and reported CV performance use the same folds, so the CV score is a selection estimate rather than an unbiased outer-CV estimate.

## Test estimates and interpretation

The main table shows single held-out scores. The feature-selection comparison resamples test encounters with replacement 100 times without refitting. Reported standard deviations are across those resamples, not standard errors, confidence intervals, retraining variation, or patient-cluster uncertainty. Repeated encounters violate the independence assumed by ordinary row-level bootstrap; patient-level bootstrap remains future work.

Absolute linear coefficients, impurity-based tree importance, and training-set permutation importance have different scales and biases. Top-feature overlap is descriptive. The feature-category helper is a string-matching summary, not a validated clinical taxonomy. No causal or clinical deployment claim follows from these figures.
