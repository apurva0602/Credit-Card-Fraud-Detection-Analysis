

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Separate genuine and fraud transactions
genuine = df[df['Class'] == 0]
fraud = df[df['Class'] == 1]

# Calculate average transaction amount
print("Average Genuine Transaction Amount:",
      round(genuine['Amount'].mean(), 2))

print("Average Fraud Transaction Amount:",
      round(fraud['Amount'].mean(), 2))

# Create box plot
plt.figure(figsize=(8, 5))

plt.boxplot(
    [genuine['Amount'], fraud['Amount']],
    tick_labels=['Genuine', 'Fraud']
)

plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Type")
plt.ylabel("Transaction Amount")

plt.tight_layout()
plt.show()
