from utils import *
from prompt_library import *
from call_llm import *
from random_items import *

import tiktoken
import tqdm
import json
import random
from typing import List

trouble = []

class SyntheticPatientData:
    """
    
    Synthetic Patient Data Class to generate synthetic patient data with a given health problem.    

    """

    def __init__(self):
        self.person_data = generate_person()
        self.doctor_data = generate_person()
        self.patient_name = self.person_data['results'][0]['name']['first'] + ' ' + self.person_data['results'][0]['name']['last']
        self.address = str(self.person_data['results'][0]['location']['street']['number']) + ' ' + self.person_data['results'][0]['location']['street']['name'] + ', ' + self.person_data['results'][0]['location']['city'] + ', ' + self.person_data['results'][0]['location']['state'] + ' ' + str(self.person_data['results'][0]['location']['postcode'])
        self.phone = self.person_data['results'][0]['phone']
        self.gender = self.person_data['results'][0]['gender']
        self.age = self.person_data['results'][0]['dob']['age']
        self.dob = extract_date(self.person_data['results'][0]['dob']['date'])
        self.doctor_name = "Dr. " + self.doctor_data['results'][0]['name']['first'] + ' ' + self.doctor_data['results'][0]['name']['last']
        self.full_patient_data = None
        self.health_problem = None
        self.patient_convo = None
        self.soap_notes = None
    
    
    def generate_patient_data(self, patient_name,age,gender,address, phone, dob, doctor_name, prompt=create_synth_patient_data_prompt, health_problems:List[str] = health_issues, model=mistral_model, temperature=0.5, max_tokens=4000):
        health_problem = random.choice(health_problems)
        self.health_problem = health_problem
        
        final_prompt = prompt.format(health_problem=health_problem, patient_name=patient_name, age=age,gender=gender,address=address, phone=phone, dob=dob, doctor_name=doctor_name)
        result = call_llm(final_prompt,model,temperature,max_tokens)
        
        self.full_patient_data = result.choices[0].text
        
        return self.full_patient_data, self.health_problem
       

    def generate_clinical_dialogue(self,prompt=create_synth_convo_prompt, model=llama_model, temperature=0.5, max_tokens=1500):
        
        final_prompt = prompt.format(patient_data= self.full_patient_data)
       
        final_prompt = final_prompt.replace("\n\n\n\n", "")
        final_prompt = final_prompt.replace("-----", "")
        final_prompt = final_prompt.replace("====", "")
        
        trouble.append(final_prompt)

        with open("trouble.json", 'w') as f:
            json.dump(trouble, f)

        

        result = call_llm(final_prompt, model, temperature, max_tokens)
        
          
        self.patient_convo = result.choices[0].text

        return self.patient_convo
    
    def create_synth_data(self):
        print("Creating Synthetic Patient Data...")
        self.generate_patient_data(self.patient_name, self.age,self.gender,self.address, self.phone, self.dob, self.doctor_name)
        print("Complete")
        
        print("Creating Synthetic Clinical Dialogue...")
        self.generate_clinical_dialogue()
        print("Complete")

    def generate_soap_notes(self, prompt=create_synth_soap_notes_prompt,model=gpt_turbo_model,temperature=0.1):
        print("Creating Synthetic SOAP Notes...")
        final_prompt = prompt.format(patient_data=self.full_patient_data, patient_convo=self.patient_convo)
       
        result = call_openai(final_prompt, model, temperature)
            
        self.soap_notes = result.choices[0].message.content
        print("Complete")
        return self.soap_notes, final_prompt
    
    def generate_soap_notes_phi(self, prompt=create_synth_soap_notes_prompt,model=phi_model,temperature=0.1):
        print("Creating Synthetic SOAP Notes...")
        final_prompt = prompt.format(patient_data=self.full_patient_data, patient_convo=self.patient_convo)
       
        result = call_phi(final_prompt, model, temperature)
            
        self.soap_notes = result.choices[0].message.content
        print("Complete")
        return self.soap_notes, final_prompt
        

def create_synthetic_data_json(total, name='synthetic_data.json'):
    list_of_patients = []
   
    
    for i in tqdm.tqdm(range(total)):
        
        patient = SyntheticPatientData()
        
        
        if patient.patient_convo is not None:
            
            patient.generate_soap_notes()
            
            list_of_patients.append(patient)

            with open(name, 'w') as f:
                json.dump([data.__dict__ for data in list_of_patients], f)
        


if __name__ == '__main__':
    create_synthetic_data_json(150,'synthetic_data_10.json')




