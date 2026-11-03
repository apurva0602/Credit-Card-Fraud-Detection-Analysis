
import pandas as pd

# Load original dataset
df = pd.read_csv(r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv")

# Create hour column
df['Hour'] = (df['Time'] // 3600).astype(int)

# Create transaction type
df['Transaction_Type'] = df['Class'].map({
    0: 'Genuine',
    1: 'Fraud'
})

# Export cleaned dataset
df.to_csv(
    r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\Fraud_Analysis_Data.csv",
    index=False
)

print("Power BI dataset exported successfully!")
print("Dataset Shape:", df.shape)
