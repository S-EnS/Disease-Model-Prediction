import os

# Define the path where the cleaned data will be saved
output_dir = '/Desktop/disease prediction model project/data/ADNI/genetic/'
output_file = 'cleaned_TOMM40_10Jun2024.csv'

# Check if the directory exists
if not os.path.exists(output_dir):
    print(f"The directory {output_dir} does not exist.")
else:
    print(f"The directory {output_dir} exists.")

# Full path to the output file
output_path = os.path.join(output_dir, output_file)
print(f"Output path: {output_path}")
