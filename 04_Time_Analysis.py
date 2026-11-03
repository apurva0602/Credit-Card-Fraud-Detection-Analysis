
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Convert seconds into hours
df['Hour'] = (df['Time'] // 3600).astype(int)

# Separate genuine and fraud transactions
genuine = df[df['Class'] == 0]
fraud = df[df['Class'] == 1]

# Count transactions per hour
genuine_count = genuine.groupby('Hour').size()
fraud_count = fraud.groupby('Hour').size()

# Plot graph
plt.figure(figsize=(12, 6))

plt.plot(genuine_count.index, genuine_count.values,
         label='Genuine Transactions')

plt.plot(fraud_count.index, fraud_count.values,
         label='Fraud Transactions')

plt.title("Transaction Activity Over Time")
plt.xlabel("Recorded Time (Hours)")
plt.ylabel("Number of Transactions")

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
