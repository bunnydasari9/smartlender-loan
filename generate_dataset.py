"""
Generates a synthetic loan_approval_dataset.csv that mirrors the structure
of the Kaggle 'Loan Approval Prediction Dataset' referenced in the guide,
including the leading-whitespace quirks in headers/text values so the
cleaning steps in the notebook/train.py have something real to fix.
"""
import numpy as np
import pandas as pd

np.random.seed(42)
N = 4269  # matches the guide's stated record count

no_of_dependents = np.random.randint(0, 6, N)
education = np.random.choice([' Graduate', ' Not Graduate'], N, p=[0.5, 0.5])
self_employed = np.random.choice([' Yes', ' No'], N, p=[0.3, 0.7])

income_annum = np.random.randint(200000, 10000000, N)
loan_amount = (income_annum * np.random.uniform(0.5, 4, N)).astype(int)
loan_term = np.random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], N)
cibil_score = np.random.randint(300, 900, N)

residential_assets_value = (income_annum * np.random.uniform(0, 1.5, N)).astype(int)
commercial_assets_value = (income_annum * np.random.uniform(0, 1.0, N)).astype(int)
luxury_assets_value = (income_annum * np.random.uniform(0, 1.8, N)).astype(int)
bank_asset_value = (income_annum * np.random.uniform(0, 0.8, N)).astype(int)

# Build an approval "risk score" driving realistic correlations, then
# threshold + noise to produce the label.
risk_score = (
    (cibil_score - 300) / 600 * 0.5
    + (1 - loan_amount / (income_annum + 1)).clip(-1, 1) * 0.25
    + (income_annum / income_annum.max()) * 0.15
    - (no_of_dependents / 5) * 0.05
    + np.random.normal(0, 0.08, N)
)

loan_status = np.where(risk_score > np.quantile(risk_score, 0.382), ' Approved', ' Rejected')

df = pd.DataFrame({
    ' loan_id': np.arange(1, N + 1),
    ' no_of_dependents': no_of_dependents,
    ' education': education,
    ' self_employed': self_employed,
    ' income_annum': income_annum,
    ' loan_amount': loan_amount,
    ' loan_term': loan_term,
    ' cibil_score': cibil_score,
    ' residential_assets_value': residential_assets_value,
    ' commercial_assets_value': commercial_assets_value,
    ' luxury_assets_value': luxury_assets_value,
    ' bank_asset_value': bank_asset_value,
    ' loan_status': loan_status,
})

df.to_csv('data/loan_approval_dataset.csv', index=False)
print(f"Synthetic dataset written: data/loan_approval_dataset.csv ({df.shape[0]} rows, {df.shape[1]} cols)")
print(df[' loan_status'].str.strip().value_counts(normalize=True) * 100)
