from difflib import SequenceMatcher
import streamlit as st

llm_output = """SOAP Note:

(Subjective, Objective, Assessment, Plan)

Subjective:
Patient presents with complaints of intense pain in the abdominal region for the past three days, initially described as a dull ache but now sharp and persistent, localized mainly on the lower right side. Patient also reports nausea and alterations in bowel movements but denies vomiting or fever.

Objective:
Physical examination reveals tenderness in the lower right quadrant of the abdomen. No signs of fever or dehydration observed. Further diagnostic tests required for confirmation.

Assessment:
Based on patient's symptoms and physical examination, differential diagnosis includes appendicitis. Further evaluation needed to confirm diagnosis.

Plan:

Order blood tests, urinalysis, and imaging studies (ultrasound or CT scan) to assess for appendicitis.
Provide patient with information on appendicitis and the necessity for prompt treatment to prevent complications.
Arrange for surgical consultation for possible appendectomy if diagnosis is confirmed.
Prescribe pain management medication to alleviate discomfort in the meantime.
Educate patient on signs of worsening symptoms and advise to seek immediate medical attention if they occur.
Schedule follow-up appointment to discuss test results and treatment plan.
Patient's willingness to cooperate with diagnostic process and understanding of potential treatment options noted. Encouraged patient to reach out with any concerns or questions.

"""

matching = "Patient also reports nausea and alterations in bowel movements but denies vomiting or fever."

# Find matching region
matcher = SequenceMatcher(None, llm_output, matching)
match = matcher.find_longest_match(0, len(llm_output), 0, len(matching))

matching_region = llm_output[match.a : match.a + match.size]

# Create HTML
highlighted_html = llm_output.replace(matching_region, f'<span style="font-weight: bold; color: green;">{matching_region}</span>')

print(highlighted_html)
print(matching_region)
print(match)
print(matcher)

st.write(highlighted_html, unsafe_allow_html=True)