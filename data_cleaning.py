import json

file_path = 'synthetic_data_10.json'

with open(file_path, 'r') as file:
    data = json.load(file)

index = []
for i in range(len(data)):
    if data[i]['full_patient_data'].find("\n\n\n\n\n\n\n") != -1:
        index.append(i)

print(index)

# Remove data[index]
for i in sorted(index, reverse=True):
    del data[i]

# Save cleaned data as synthetic_data_1_cleaned.json
cleaned_file_path = 'synthetic_data_10_cleaned.json'
with open(cleaned_file_path, 'w') as file:
    json.dump(data, file)


