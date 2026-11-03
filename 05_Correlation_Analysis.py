
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Calculate correlation
correlation = df.corr()

# Create heatmap
plt.figure(figsize=(16, 12))

plt.imshow(correlation, cmap='coolwarm', aspect='auto')

plt.colorbar(label='Correlation')

plt.title("Credit Card Transaction Correlation Heatmap")
plt.xticks(range(len(correlation.columns)),
           correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.tight_layout()
plt.show()

# Show features most correlated with fraud
print("\nCorrelation with Fraud:")
print(correlation['Class'].sort_values(ascending=False))
