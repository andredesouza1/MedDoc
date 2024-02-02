import streamlit as st
from ST_sentence_match import create_sentence_array, has_sentence_ending_punctuation
import ST_sentence_match
from difflib import SequenceMatcher
from sorted_sentence_select import binary_search_score

st.set_page_config(layout="wide")

st.title("Sentence Highlighter")

sentence_selector = st.selectbox("Select a sentence" , ST_sentence_match.llm_output_sentences)

min_score = st.slider("Minimum score", 0.3, 0.8, 0.5, 0.01)

col1, col2= st.columns(2)

matcher_output = SequenceMatcher(None, ST_sentence_match.llm_output, sentence_selector)
match_output = matcher_output.find_longest_match(0, len(ST_sentence_match.llm_output), 0, len(sentence_selector))

matching_region_output = ST_sentence_match.llm_output[match_output.a : match_output.a + match_output.size]

# Create HTML
highlighted_html_output = ST_sentence_match.llm_output.replace(matching_region_output, f'<span style="font-weight: bold; color: blue;">{matching_region_output}</span>')

matching_output_sentence_index= []

#Can add a button if you want here
min_score_index = binary_search_score(min_score, ST_sentence_match.sorted_sentence_pairs_by_score)
    
for i in range(len(ST_sentence_match.sorted_sentence_pairs_by_score[min_score_index:])):
    if ST_sentence_match.sorted_sentence_pairs_by_score[min_score_index+i][1] == sentence_selector:
        matching_output_sentence_index.append(min_score_index+i)
        

def match_output_to_input(sentence_list, matching_output_sentence_index):
    matching_region_input_list = []
    for i in range(len(matching_output_sentence_index)):
        matcher_input = SequenceMatcher(None, ST_sentence_match.llm_input, sentence_list[matching_output_sentence_index[i]][0])
        match_input = matcher_input.find_longest_match(0, len(ST_sentence_match.llm_input), 0, len(sentence_list[matching_output_sentence_index[i]][0]))

        matching_region_input = ST_sentence_match.llm_input[match_input.a : match_input.a + match_input.size]
        matching_region_input_list.append(matching_region_input)
    
    # Create HTML
    highlighted_html_input = ST_sentence_match.llm_input
    for matching_region_input in matching_region_input_list:
        highlighted_html_input = highlighted_html_input.replace(matching_region_input, f'<span style="font-weight: bold; color: green;">{matching_region_input}</span>')

    return highlighted_html_input

if matching_output_sentence_index:
    highlighted_html_input = match_output_to_input(ST_sentence_match.sorted_sentence_pairs_by_score, matching_output_sentence_index)
else:
    highlighted_html_input = ST_sentence_match.llm_input


with col2:
    st.header("Output")
    
    st.write(highlighted_html_output, unsafe_allow_html=True)
    st.write(matching_output_sentence_index)

with col1:
    st.header("Input" )
    st.write(highlighted_html_input, unsafe_allow_html=True)

