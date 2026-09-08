import re

import spacy
from pypdf import PdfReader


# spaCy English model load karo
nlp = spacy.load("en_core_web_sm")


# Skills list
SKILLS = [
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",

    "react",
    "angular",
    "vue",

    "html",
    "css",

    "flask",
    "fastapi",
    "django",

    "sql",
    "postgresql",
    "mysql",
    "mongodb",

    "git",
    "github",
    "docker",
    "kubernetes",

    "machine learning",
    "deep learning",

    "natural language processing",
    "nlp",

    "scikit-learn",
    "tensorflow",
    "pytorch",

    "pandas",
    "numpy",

    "excel",

    "statistics",
    "data analysis",
    "data visualization",

    "rest api",
    "api",

    "aws",
    "azure",
    "gcp"
]


def extract_pdf_text(file_path):
    """
    PDF se text extract karta hai.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def normalize_text(text):
    """
    Text ko clean aur normalize karta hai.
    """

    # Lowercase
    text = text.lower()

    # Extra spaces remove
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def extract_skills(text):
    """
    CV text mein available skills find karta hai.
    """

    normalized_text = normalize_text(text)

    found_skills = []

    for skill in SKILLS:

        pattern = (
            r"\b"
            + re.escape(skill.lower())
            + r"\b"
        )

        if re.search(
            pattern,
            normalized_text
        ):
            found_skills.append(skill)

    return sorted(
        set(found_skills)
    )


def extract_entities(text):
    """
    spaCy NER ke through entities extract karta hai.
    """

    doc = nlp(text)

    entities = []

    for entity in doc.ents:

        entities.append({
            "text": entity.text,
            "label": entity.label_
        })

    return entities


def parse_cv(file_path):
    """
    Complete CV parsing pipeline.
    """

    # PDF se text
    raw_text = extract_pdf_text(
        file_path
    )

    # Check text
    if not raw_text.strip():

        raise ValueError(
            "Could not extract text from the PDF."
        )

    # Clean text
    cleaned_text = normalize_text(
        raw_text
    )

    # Skills
    skills = extract_skills(
        cleaned_text
    )

    # Named entities
    entities = extract_entities(
        raw_text
    )

    return {
        "text": cleaned_text,
        "skills": skills,
        "entities": entities
    }