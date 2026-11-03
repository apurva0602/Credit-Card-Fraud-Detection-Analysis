# Credit Card Fraud Detection & Analysis

## Project Overview
This project focuses on analyzing credit card transactions to identify patterns associated with fraudulent activities using Python and Power BI.

## Objectives
- Analyze fraudulent and genuine transactions.
- Identify transaction amount patterns.
- Study recorded transaction time patterns.
- Build an interactive Power BI dashboard.
- Recommend triggers for a real-time fraud alert system.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Power BI
- SQL (if used in a future extension)

## Dataset
ULB Credit Card Fraud Detection Dataset from Kaggle.

- Total Transactions: 284,807
- Fraud Transactions: 492
- Genuine Transactions: 284,315
## Dataset Source

The dataset used in this project is publicly available on Kaggle.

Download here:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Note: The original dataset is not included in this repository due to its large file size.

## Key Findings
- Fraud transactions have a higher average amount ($122.21) than genuine transactions ($88.29).
- Fraud transactions have a lower median amount ($9.25) than genuine transactions ($22.00).
- Fraudulent transactions include both small and high-value amounts.
- Transaction patterns can help design risk-based fraud alerts.

## Dashboard
The Power BI dashboard includes:
- Total Transactions
- Fraud Transactions
- Genuine Transactions
- Fraud Percentage
- Fraud vs Genuine Distribution
- Transaction Amount Analysis
- Recorded Time Analysis
## Power BI Dashboard

The interactive Power BI dashboard created for this project can be accessed below:

[Download Credit Card Fraud Analysis Dashboard (.pbix)](https://drive.google.com/file/d/1EL5pQh2nYBgrLSYbyYBzCLE3o4y7ZGE1/view?usp=sharing)

## Real-Time Fraud Alert Recommendations
- Flag unusually high transaction amounts.
- Monitor suspicious transaction patterns.
- Generate alerts when multiple risk signals appear.
- Apply additional authentication to high-risk transactions.

## Conclusion
This project demonstrates how data analysis and visualization can help understand credit card fraud patterns and support fraud monitoring strategies.

*Note: The alert recommendations are proposed ideas and have not been validated as a production fraud detection model.*
