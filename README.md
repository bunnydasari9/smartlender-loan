# Smart Lender: Loan Approval Prediction System

This is the working implementation built from the "Smart Lender ML Guide."

## Setup
```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost joblib flask
```

## Dataset
A synthetic `data/loan_approval_dataset.csv` is included (4,269 rows, same schema
as the Kaggle "Loan Approval Prediction Dataset" referenced in the guide, including
the leading-whitespace quirks in headers/values). Swap in the real Kaggle CSV at
the same path if you prefer — the code works either way.

To regenerate the synthetic dataset: `python3 generate_dataset.py`

## Train the model
```bash
python train.py
```
This compares Logistic Regression, Random Forest, and XGBoost, then saves the
winning model + scaler to `models/`.

## Run the web app
```bash
python app.py
```
Visit http://localhost:5000

## Note on pandas 3.0 compatibility
If you have pandas 3.0+ installed, string columns default to a new `str` dtype
instead of the legacy `object` dtype. The original guide's whitespace-stripping
check (`df[col].dtype == 'object'`) silently skips these columns on pandas 3.0+,
which causes a `ValueError: Input y contains NaN` later in the pipeline. This has
been patched in `train.py` and `notebook.ipynb` to check both dtypes:
```python
if df[col].dtype == 'object' or pd.api.types.is_string_dtype(df[col]):
    df[col] = df[col].str.strip()
```

## Verified
- `train.py` pipeline runs end-to-end (verified locally with a fallback classifier
  in place of XGBoost, since this sandbox has no internet to install it — your
  local install will use real XGBoost per the script).
- `app.py`'s `/predict` endpoint tested against both scenarios from the guide's
  Part 8.5: the low-risk profile returned "approved" with ~99.9% confidence, and
  the high-risk profile returned "rejected" with ~99.2% confidence.
