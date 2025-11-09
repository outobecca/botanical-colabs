# Import necessary libraries
import pandas as pd

# Define the scientific name for data collection
scientific_name = "Convallaria majalis"

# Fetch occurrence data from GBIF using the provided function
occurrence_records = fetch_gbif_occurrence_data(scientific_name)

# Check if data was successfully retrieved.  Handle potential errors gracefully.
if occurrence_records is None:
    print(f"Error: Could not retrieve occurrence data for {scientific_name}. Please check the GBIF API or your internet connection.")
    exit() # Exit the script if no data is retrieved

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(occurrence_records)

# Print the first 5 rows of the DataFrame to inspect the data
print("First 5 rows of the DataFrame:")
print(df.head())

# Print the shape (number of rows and columns) of the DataFrame
print("\nShape of the DataFrame:", df.shape)
