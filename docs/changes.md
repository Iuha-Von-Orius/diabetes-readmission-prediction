# Packaging and execution changes

The public copy keeps the original analysis sequence, model families, target definition, seed, default split fractions, hyperparameter grids, and bootstrap budget.

- Replace administrative headings and prompts with technical sections; remove private paths, environment metadata, original report files, and stale embedded outputs.
- Use local relative data paths, include unmodified public CSV inputs with attribution, and keep one main notebook.
- Define score extraction before its first use. Remove duplicate plots, an unused intermediate preprocessor, an abandoned split, and a broken string-arithmetic summary; retain the existing numeric performance-change calculation.
- Correct encounter/column terminology and keep a single consistent uppercase target mapping.
- Normalize string-column storage for compatibility with newer pandas versions while preserving the original CSV NA parsing.
- Clone preprocessors per model pipeline to avoid shared fitted state. Read feature counts from the fitted selection pipeline rather than refitting a shared preprocessor.
- Inherit selected random forest parameters rather than duplicating fixed values in the selector. Keep random forest explicitly as the feature-selection model family.
- Replace the correlation heatmap's plotting dependency with Matplotlib, preserving the correlation calculation.
- Add an opt-in reduced smoke mode and skip ROC-AUC computation only for single-class bootstrap samples. Default full-data settings remain unchanged.
- Preserve recorded historical metrics separately from current-run outputs, and expose patient overlap rather than claiming patient-disjoint evaluation.

No new full-data model results are claimed. Alternative patient-grouped splits, different NA handling, fully fold-local column dropping, and changed feature semantics would be separate experiments.
