from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

# Single list of sentences
sentences1 = [
    "The cat sits outside",
    "A man is playing guitar",
    "I love pasta",
    "The new movie is awesome",
    "The cat plays in the garden",
    "A woman watches TV",
    "The new movie is so great",
    "Do you like pizza?",
]

sentences2 = [
    "The birds chirp in the morning.",
    "An old man reads the newspaper.",
    "She enjoys hiking in the mountains.",
    "The delicious smell of coffee fills the room.",
    "A group of friends gathers around the bonfire.",
    "He rides his bike through the park.",
    "The sun sets behind the horizon, painting the sky orange.",
    "Children laugh and play in the playground."
]


# Compute embedding for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)

# Output the pairs with their score
for i in range(len(sentences1)):
    print("{} \t\t {} \t\t Score: {:.4f}".format(
        sentences1[i], sentences2[i], cosine_scores[i][i]
    ))