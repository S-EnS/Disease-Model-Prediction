import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

# Load SNP data from a CSV file
snp_data = pd.read_csv('/Users/enes/Desktop/disease_prediction_model_project/data/ADNI/genetic/cleaned_TOMM40_10Jun2024.csv')

# For demonstration, let's create a dummy phenotype column (1 for disease presence, 0 for absence)
# Replace this with actual phenotype data when available
snp_data['SNPS'] = [1 if i % 2 == 0 else 0 for i in range(len(snp_data))]

# Separate features (SNPs) and target (phenotype)
X = snp_data.drop(columns=['', '0'])  # Exclude non-numeric columns
y = snp_data['SNPS']  # Replace 'phenotype' with the actual column name for phenotype data

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Get feature importances
feature_importances = rf.feature_importances_

# Create a DataFrame to hold feature names and their importance scores
importance_df = pd.DataFrame({'SNP': X.columns, 'Importance': feature_importances})

# Sort the DataFrame by importance scores in descending order
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Display the top 10 important features
print("Top 10 important features based on Random Forest:")
print(importance_df.head(10))

# Save the feature importance ranking to a CSV file
output_dir = '/Users/enes/Desktop/disease_prediction_model_project/data/ADNI/genetic/'
output_file = 'snp_feature_importance_rf.csv'
output_path = os.path.join(output_dir, output_file)
importance_df.to_csv(output_path, index=False)
print(f"Feature importance ranking saved successfully to {output_path}")
