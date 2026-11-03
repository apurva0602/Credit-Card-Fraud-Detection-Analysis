
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Separate transactions
genuine = df[df['Class'] == 0]
fraud = df[df['Class'] == 1]

# Compare transaction amounts
print("\n--- Average Transaction Amount ---")
print("Genuine:", round(genuine['Amount'].mean(), 2))
print("Fraud:", round(fraud['Amount'].mean(), 2))

# Compare median amounts
print("\n--- Median Transaction Amount ---")
print("Genuine:", round(genuine['Amount'].median(), 2))
print("Fraud:", round(fraud['Amount'].median(), 2))

# Compare standard deviation
print("\n--- Amount Variation ---")
print("Genuine:", round(genuine['Amount'].std(), 2))
print("Fraud:", round(fraud['Amount'].std(), 2))

# Compare transaction time
print("\n--- Average Transaction Time ---")
print("Genuine:", round(genuine['Time'].mean(), 2))
print("Fraud:", round(fraud['Time'].mean(), 2))

# Statistical summary
print("\n--- Fraud Transaction Summary ---")
print(fraud[['Time', 'Amount']].describe())
