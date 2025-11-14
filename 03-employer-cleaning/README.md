# Employer Cleaning (Synthetic)

A small utility to standardize messy employer names from applications.

## What's here
- `data/raw_employers.csv` — synthetic messy employer strings.
- `src/clean_employers.py` — normalization and canonical mapping (no external deps).
- `outputs/employers_clean.csv` — cleaned results (create by running the script).

> Approach: lowercase → strip punctuation → expand common variants → map to canonical labels.
