import pandas as pd
import os

try:
    # Load SNP data from a CSV file
    snp_data = pd.read_csv('TOMM40_10Jun2024.csv')
    print("Loaded SNP data successfully.")

    # Calculate the proportion of missing values for each SNP (column)
    missingness_per_snp = snp_data.isnull().mean()

    # Calculate the proportion of missing values for each sample (row)
    missingness_per_sample = snp_data.isnull().mean(axis=1)

    # Define a threshold for acceptable missingness (e.g., 5%)
    missingness_threshold_snp = 0.05
    missingness_threshold_sample = 0.05

    # Identify SNPs to keep
    snps_to_keep = missingness_per_snp[missingness_per_snp <= missingness_threshold_snp].index

    # Filter out SNPs with high missingness
    filtered_snp_data = snp_data[snps_to_keep]
    print("Filtered SNP data successfully.")

    # Identify samples to keep
    samples_to_keep = missingness_per_sample[missingness_per_sample <= missingness_threshold_sample].index

    # Filter out samples with high missingness
    filtered_snp_data = filtered_snp_data.loc[samples_to_keep]
    print("Filtered samples successfully.")

    # Display the filtered data
    print(filtered_snp_data.head())

    # Define the output directory and file
    output_dir = '/Users/enes/Desktop/disease_prediction_model_project/data/ADNI/genetic/'
    output_file = 'cleaned_TOMM40_10Jun2024.csv'
    
    # Create the directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    else:
        print(f"Directory already exists: {output_dir}")

    # Full path to the output file
    output_path = os.path.join(output_dir, output_file)
    print(f"Output path: {output_path}")

    # Save the cleaned dataset to a new CSV file
    filtered_snp_data.to_csv(output_path, index=False)
    print(f"Cleaned data saved successfully to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")
