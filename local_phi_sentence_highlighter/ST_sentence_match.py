from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


llm_input = """Based on the following conversation create a SOAP:

Doctor: Good morning, how can I help you today?

Patient: Hi doctor, I've been experiencing some intense pain in my abdominal region for the past couple of days, and it's really worrying me.

Doctor: I'm sorry to hear that. Can you tell me more about the pain? When did it start, and how would you describe it?

Patient: It started about three days ago. At first, it was just a dull ache, but now it's become quite sharp and persistent. It's mainly on the lower right side of my abdomen.

Doctor: Okay, have you noticed any other symptoms accompanying the pain? Such as nausea, vomiting, fever, or changes in bowel movements?

Patient: Yes, I've been feeling nauseous, and I've had some trouble with my bowel movements as well. No vomiting or fever though.

Doctor: Alright, based on your description, it's possible that you're experiencing appendicitis, which is inflammation of the appendix. However, we'll need to conduct some tests to confirm.

Patient: Appendicitis? Is that serious?

Doctor: It can be if left untreated, as it can lead to complications such as a ruptured appendix. But don't worry, if it is appendicitis, the most common treatment is surgical removal of the appendix, which is a routine procedure.

Patient: Surgery? That sounds scary.

Doctor: I understand your concerns, but appendectomy, the surgical removal of the appendix, is a very common and safe procedure. It's important to address this promptly to avoid any potential complications.

Patient: Okay, what tests do we need to do to confirm if it's appendicitis?

Doctor: We'll start with a physical examination to assess your symptoms and perform some diagnostic tests such as blood tests, urinalysis, and possibly imaging studies like an ultrasound or CT scan to get a clearer picture of what's going on inside your abdomen.

Patient: Alright, let's do whatever it takes to figure this out and get it treated. The pain is really becoming unbearable.

Doctor: Absolutely, your health and well-being are our top priority. We'll work together to get to the bottom of this and get you feeling better soon. I'll arrange for the necessary tests and keep you informed every step of the way.

Patient: Thank you, doctor. I appreciate your help and reassurance.

Doctor: You're welcome. We're here to support you through this process. If you have any questions or concerns at any point, don't hesitate to reach out."""



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




def create_sentence_array(sentence):
    words = []
    words = sentence.split()
    sentences = []
    local_string = ''

    for word in words:
        if has_sentence_ending_punctuation(word):
            local_string = local_string + ' ' + word
            sentences.append(local_string)
            local_string = ''
        else:
            local_string = local_string + ' '+ word
    return sentences 


def has_sentence_ending_punctuation(text):
    sentence_ending_punctuation = {'.', '?', '!', ':'}
    for char in text:
        if char in sentence_ending_punctuation:
            return True
    return False

llm_input_sentences = create_sentence_array(llm_input)

llm_output_sentences = create_sentence_array(llm_output)

# Compute embedding for both lists
embeddings1 = model.encode(llm_input_sentences, convert_to_tensor=True)
embeddings2 = model.encode(llm_output_sentences, convert_to_tensor=True)

# Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)


# Create a list of tuples containing the sentence pairs and their corresponding cosine scores
sentence_pairs = []
for i in range(len(llm_input_sentences)):
    for j in range(len(llm_output_sentences)):
        sentence_pairs.append((llm_input_sentences[i], llm_output_sentences[j], cosine_scores[i][j]))

# Sort the sentence pairs based on the cosine scores in ascending order
sorted_sentence_pairs_by_score = sorted(sentence_pairs, key=lambda x: x[2])
sorted_sentence_pairs_by_output = sorted(sentence_pairs, key=lambda x: x[1])


# # Print the sentence pairs in order of lowest to highest cosine scores
# for pair in sorted_sentence_pairs:
#     print("{} \t\t {} \t\t Score: {:.4f}".format(pair[0], pair[1], pair[2]))

# print(sorted_sentence_pairs_by_output)