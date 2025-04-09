import pandas as pd

# Use on_bad_lines='skip' to skip lines with too many fields
df = pd.read_csv(r"C:\Users\leemi\OneDrive - North-West University\Honours Resources\School\2025\First Semester\ITRI 616 (Artificial Inteligence)\Assignment\ML_ Classification Project\ML-Classification-Project\Dataset\apartments_for_rent_classified_10K.csv", encoding='ISO-8859-1', on_bad_lines='skip')

# Show the first few rows of the full dataframe
print("\n--- Full Data Preview ---")
print(df.head())

# Separate features and target (adjust the target column name accordingly)
# Example: assuming the last column is the target
X = df.iloc[:, :-1]  # All columns except the last
y = df.iloc[:, -1]   # Last column (assumed target)

# Display features and target previews
print("\n--- Features (X) Preview ---")
print(X.head())

print("\n--- Target (y) Preview ---")
print(y.head())

# Show "metadata" style info
print("\n--- Metadata ---")
print(f"Number of samples: {df.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Target column: {df.columns[-1]}")

# Show variable information
print("\n--- Variable Information ---")
print(df.dtypes)
