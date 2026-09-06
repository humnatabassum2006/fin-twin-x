from sentence_transformers import SentenceTransformer
import numpy as np


# =========================================================
# LOAD EMBEDDING MODEL
# =========================================================

model = SentenceTransformer("all-MiniLM-L6-v2")


# =========================================================
# LOAD KNOWLEDGE BASE
# =========================================================

KNOWLEDGE_BASE_PATH = "knowledge_base/financial_guidelines.txt"


def load_knowledge_base():
    with open(
        KNOWLEDGE_BASE_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        knowledge = file.read()

    return knowledge


# =========================================================
# CREATE KNOWLEDGE CHUNKS
# =========================================================

def create_chunks():
    knowledge = load_knowledge_base()

    chunks = []

    for section in knowledge.split("\n\n"):

        lines = section.strip().split("\n")

        if len(lines) <= 1:
            continue

        title = lines[0]

        for line in lines[1:]:
            line = line.strip()

            if line:
                chunks.append(
                    f"{title}\n{line}"
                )

    return chunks


# =========================================================
# CREATE EMBEDDINGS
# =========================================================

def create_embeddings(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings


# =========================================================
# SEMANTIC SEARCH
# =========================================================

def semantic_search(query):

    chunks = create_chunks()

    embeddings = create_embeddings(chunks)

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )[0]

    similarities = np.dot(
        embeddings,
        query_embedding
    ) / (
        np.linalg.norm(embeddings, axis=1)
        * np.linalg.norm(query_embedding)
    )

    best_index = np.argmax(similarities)

    return chunks[best_index]