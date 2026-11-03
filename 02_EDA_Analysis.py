
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Count transactions
transaction_count = df['Class'].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    ['Genuine', 'Fraud'],
    [transaction_count[0], transaction_count[1]]
)

# Add chart title and labels
plt.title("Genuine vs Fraud Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")

# Display values on bars
for i, value in enumerate([transaction_count[0], transaction_count[1]]):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()
