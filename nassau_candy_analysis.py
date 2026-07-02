# Nassau Candy Distributor Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicate Rows
df = df.drop_duplicates()

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe(include='all'))

# Display Column Names
print("\nColumns:")
print(df.columns)

# Count Plot for First Column
first_col = df.columns[0]

plt.figure(figsize=(8,5))
df[first_col].value_counts().head(10).plot(kind='bar')
plt.title(f"Top 10 {first_col}")
plt.xlabel(first_col)
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram for Numerical Columns
num_cols = df.select_dtypes(include=['int64','float64']).columns

for col in num_cols:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=20)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Correlation Matrix
if len(num_cols) > 1:
    corr = df[num_cols].corr()

    plt.figure(figsize=(8,6))
    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()
    plt.xticks(range(len(num_cols)), num_cols, rotation=90)
    plt.yticks(range(len(num_cols)), num_cols)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

print("\nData Analysis Completed Successfully!")
