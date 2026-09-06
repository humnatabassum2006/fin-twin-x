import os


# =========================================================
# LOAD FINANCIAL KNOWLEDGE BASE
# =========================================================

KNOWLEDGE_BASE_PATH = "knowledge_base/financial_guidelines.txt"


def load_knowledge_base():
    """
    Load financial knowledge from the knowledge base.
    """

    if not os.path.exists(KNOWLEDGE_BASE_PATH):
        return ""

    with open(
        KNOWLEDGE_BASE_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        knowledge = file.read()

    return knowledge


# =========================================================
# SIMPLE RETRIEVER
# =========================================================

def retrieve_knowledge(query):
    """
    Retrieve relevant financial knowledge
    based on keywords in the user's question.
    """

    knowledge = load_knowledge_base()

    if not knowledge:
        return "Knowledge base is empty."

    query = query.lower()

    sections = knowledge.split("\n\n")

    relevant_sections = []

    keywords = [
        "save",
        "saving",
        "savings",
        "emergency",
        "debt",
        "financial health",
        "financial stress",
        "risk",
        "recommendation"
    ]

    for section in sections:

        section_lower = section.lower()

        for keyword in keywords:

            if keyword in query and keyword in section_lower:

                if section not in relevant_sections:
                    relevant_sections.append(section)

                break

    if not relevant_sections:
        return (
            "No specific financial guideline was found "
            "for this question."
        )

    return "\n\n".join(relevant_sections)