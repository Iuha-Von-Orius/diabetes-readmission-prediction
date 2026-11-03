# Dataset provenance

Source: [Diabetes 130-US Hospitals for Years 1999-2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008), UCI Machine Learning Repository. DOI: https://doi.org/10.24432/C5230J.

Citation: Clore, J., Cios, K., DeShazo, J., and Strack, B. (2014). Diabetes 130-US Hospitals for Years 1999-2008 [Dataset].

The provider lists this dataset under the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/). These CSV files are redistributed unmodified from the available local dataset copy; transformations happen in memory in the notebook.

- `diabetic_data.csv`: 101,766 hospital encounters, 50 raw columns including `readmitted`, `encounter_id`, and `patient_nbr`.
- `IDs_mapping.csv`: admission, discharge, and source-code descriptions. Its filename preserves the local copy's casing. The file contains multiple mapping sections and is used for reference, not joined as a flat lookup.

The analysis maps `NO` to 0 and combines `<30` with `>30` as 1. The CSV's repeated patient identifiers are relevant to the evaluation limits. Model-input identifiers are dropped; the published data itself remains unmodified.

Dataset credit is retained for attribution. This dataset license is distinct from any licensing decision for the analysis code.
