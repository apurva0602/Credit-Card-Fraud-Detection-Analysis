
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Create transaction amount ranges
bins = [0, 10, 50, 100, 500, 1000, 5000, float('inf')]

labels = [
    '0-10',
    '10-50',
    '50-100',
    '100-500',
    '500-1000',
    '1000-5000',
    '5000+'
]

df['Amount_Range'] = pd.cut(
    df['Amount'],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Calculate fraud percentage in each range
analysis = df.groupby(
    'Amount_Range', observed=False
).agg(
    Total_Transactions=('Class', 'count'),
    Fraud_Transactions=('Class', 'sum')
)

analysis['Fraud_Percentage'] = (
    analysis['Fraud_Transactions'] /
    analysis['Total_Transactions'] * 100
)

print("\nAmount Range Analysis:")
print(analysis.round(3))

# Plot fraud percentage
plt.figure(figsize=(10, 5))

plt.bar(
    analysis.index.astype(str),
    analysis['Fraud_Percentage']
)

plt.title("Fraud Percentage by Transaction Amount Range")
plt.xlabel("Transaction Amount Range")
plt.ylabel("Fraud Percentage (%)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()
