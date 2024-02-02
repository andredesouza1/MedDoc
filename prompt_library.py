# Create Synthetic Conversations

create_synth_convo_prompt = """
{patient_data}

Generate a clinical dialogue between a physician and a patient corresponding data provided earlier. The patient is articulating their symptoms, and the physician is engaging in a thorough inquiry to gain a comprehensive understanding of the patient's condition. The conversation should encompass the patient's subjective experiences, with the physician asking pertinent questions to elicit detailed information. The resulting conversation should not be formatted into sections but be a freeform formal conversation that would realistically happen at the doctors office. The resulting clinical dialogue is intended to serve as a precursor to the SOAP notes, capturing the essential details that form the basis of the subsequent documentation.

"""

create_synth_patient_data_prompt = """
Generate a detailed set of sample patient health record data based on the following health problem.  The resulting output should provide comprehensive patient data, including background information, medical history, current symptoms, vital signs, and any other pertinent details that contribute to a holistic understanding of the patient's health. The goal is to create a raw set of patient clinical data in a format that resembles a medical record, capturing both subjective and objective elements.
Make up any other names, addresses, phone numbers, and other details as needed. The health problem is: {health_problem}.

PATIENT INFORMATION:
Pateint Name: {patient_name}
Age: {age}
Gender: {gender}
Address: {address}
Phone: {phone}
DOB: {dob}
Doctor Name: {doctor_name}


ONLY INCLUDE THE FOLLOWING:


Demographics: name, age, address, phone number
Problem list: chronic, other
Health maintenance: vaccines and screenings, (overdue, due on.., due soon)
Reminders and Results:
Care Team and Communication:
Allergies:
Medications: name, dosage
Immunizations:
Significant History Details: tobacco use, alcohol use, language they speak 
Specialty Comments:
Family Comments:

"""

create_synth_soap_notes_prompt = """
EXAMPLE SOAP NOTE:

Subjective section
David states that he continues to experience cravings for heroin. He desperately wants to drop out of his methadone program and revert to what he was doing. David is motivated to stay sober by his daughter and states that he is "sober, but still experiencing terrible withdrawals" He stated that [he] "dreams about heroin all the time, and constantly wakes in the night drenched in sweat."

Objective observations
David was prompt to his appointment; he filled out his patient information sheet quietly in the waiting room and was pleasant during the session. He did not display signs of being under the influence. David remains aroused and distractible, but his concentration has improved. This was indicated through his discussion with me about his partner for fifteen minutes and his ability to reflect on his history. David's personal hygiene and self-care have markedly improved. His physical exam report demonstrated that he had gained 3pounds.

Assessment Section
David is making significant progress. He applies skills such as control techniques, exercises and he is progressing in his treatment. His cravings have reduced from "constant" to "a few times an hour." David continues to experience regular cravings with a 5-year history of heroin use. David needs to acquire and employ additional coping skills to stay on the same path. David is doing well, but there is significant clinical reasoning to state that David would benefit from CBT treatment as well as extended methadone treatment.

Plan
David has received a significant amount of psychoeducation within his therapy session. The therapist will begin to use dialectical behavioral therapy techniques to address David's emotion dysregulation. David also agreed to continue to hold family therapy sessions with his wife. Staff will continue to monitor David regularly in the interest of patient care and his past medical history.

Generate SOAP notes, encompassing the 'Subjective,' 'Objective,' 'Assessment,' and 'Plan' sections, based on a clinical dialogue between a physician and a patient. The patient articulates their symptoms, and the physician engages in a thorough inquiry to gain a comprehensive understanding of the patient's condition. The conversation encompasses the patient's subjective experiences, with the physician asking pertinent questions to elicit detailed information. The resulting SOAP notes should be structured into 'Subjective,' 'Objective,' 'Assessment,' and 'Plan' sections, capturing the essential details discussed in the conversation. Here is the clinical dialogue between a physician and a patient for context: 

Patient Data:
{patient_data}

Clinical Conversation:

{patient_convo}

"""


create_synth_soap_notes_prompt_phi2_train ="""
Generate SOAP notes, encompassing the 'Subjective,' 'Objective,' 'Assessment,' and 'Plan' sections, based on a clinical dialogue between a physician and a patient. The patient articulates their symptoms, and the physician engages in a thorough inquiry to gain a comprehensive understanding of the patient's condition. The conversation encompasses the patient's subjective experiences, with the physician asking pertinent questions to elicit detailed information. The resulting SOAP notes should be structured into 'Subjective,' 'Objective,' 'Assessment,' and 'Plan' sections, capturing the essential details discussed in the conversation. Here is the clinical dialogue between a physician and a patient for context: 

Patient Data:
{patient_data}

Clinical Conversation:
{patient_convo}



"""