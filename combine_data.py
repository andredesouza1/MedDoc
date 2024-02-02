import json

# List of file paths to be combined
file_paths = [
    "synthetic_data_1_cleaned.json",
    "synthetic_data_2_cleaned.json",
    "synthetic_data_3_cleaned.json",
    "synthetic_data_4_cleaned.json",
    "synthetic_data_5_cleaned.json",
    "synthetic_data_6_cleaned.json",
    "synthetic_data_7_cleaned.json",
    "synthetic_data_8_cleaned.json",
    "synthetic_data_9_cleaned.json",
    "synthetic_data_10_cleaned.json"
]

# List to store the combined data
combined_data = []

# Read each file and append its contents to the combined_data list
for file_path in file_paths:
    with open(file_path, "r") as file:
        data = json.load(file)
        combined_data.extend(data)

# Save the combined data to a new file
with open("combined_data.json", "w") as file:
    json.dump(combined_data, file)
