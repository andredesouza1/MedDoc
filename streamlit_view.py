import streamlit as st


st.title('View Output')

generate_clinical_data= st.button('Create Synthetic Data')

from generate_data import SyntheticPatientData
person = SyntheticPatientData()

if generate_clinical_data:
    person.create_synth_data()
    person.generate_soap_notes()


st.header('Patient Data')

st.write(person.full_patient_data)


st.header('Clinical Dialogue')

st.write(person.patient_convo)



st.header('SOAP Notes')

st.write(person.soap_notes)