import pandas as pd

path = r"C:\Users\apurv\OneDrive\Desktop\Credit_Card_Fraud_Analysis\Dataset\creditcard.csv"

df = pd.read_csv(path)

fraud = df[df["Class"] == 1]
genuine = df[df["Class"] == 0]

print("TOTAL FRAUD TRANSACTIONS:", len(fraud))
print("TOTAL GENUINE TRANSACTIONS:", len(genuine))

print("\nAVERAGE TRANSACTION AMOUNT")
print("Fraud:", fraud["Amount"].mean())
print("Genuine:", genuine["Amount"].mean())

print("\nMEDIAN TRANSACTION AMOUNT")
print("Fraud:", fraud["Amount"].median())
print("Genuine:", genuine["Amount"].median())

print("\nFRAUD TRANSACTION TIME DETAILS")
print(fraud["Time"].describe())

print("\nFRAUD AMOUNT DETAILS")
print(fraud["Amount"].describe())