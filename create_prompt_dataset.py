from prompt_library import *
import json

file_path = "combined_data.json"

with open(file_path, "r") as file:
    data = json.load(file)

new_data = []

for i, item in enumerate(data):
    patient_data = item['full_patient_data']
    patient_convo = item['patient_convo']
    soap_notes = item['soap_notes']

    result = create_synth_soap_notes_prompt_phi2_train.format(patient_data=patient_data, patient_convo=patient_convo)

    new_data.append({'number': i, 'messages': [result, soap_notes]})

with open("prompt_dataset/train.json", "w") as file:
    json.dump(new_data, file)



