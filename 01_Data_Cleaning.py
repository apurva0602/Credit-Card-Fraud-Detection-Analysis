
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# 1. Check dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# 2. Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# 3. Check dataset information
print("\nDataset Information:")
df.info()

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check transaction class distribution
print("\nTransaction Distribution:")
print(df['Class'].value_counts())

# Calculate fraud and genuine transactions
fraud = df[df['Class'] == 1].shape[0]
genuine = df[df['Class'] == 0].shape[0]

print("\nFraud Transactions:", fraud)
print("Genuine Transactions:", genuine)

# Calculate fraud percentage
fraud_percentage = (fraud / len(df)) * 100

print("Fraud Percentage:", round(fraud_percentage, 3), "%")