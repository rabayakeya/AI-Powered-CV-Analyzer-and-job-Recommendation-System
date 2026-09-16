import json
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_jobs():
    """
    Load jobs from jobs.json.
    """

    file_path = os.path.join(
        os.path.dirname(__file__),
        "jobs.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def recommend_jobs(cv_text, top_n=5):
    """
    Compare CV text with job descriptions
    using TF-IDF and cosine similarity.
    """

    jobs = load_jobs()

    if not cv_text.strip():
        return []

    job_texts = []

    for job in jobs:

        skills = " ".join(job.get("skills", []))

        description = job.get(
            "description",
            ""
        )

        combined_text = (
            job.get("title", "")
            + " "
            + description
            + " "
            + skills
        )

        job_texts.append(combined_text)

    documents = [cv_text] + job_texts

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    cv_vector = tfidf_matrix[0]

    job_vectors = tfidf_matrix[1:]

    similarities = cosine_similarity(
        cv_vector,
        job_vectors
    )[0]

    recommendations = []

    for index, score in enumerate(similarities):

        job = jobs[index].copy()

        match_percentage = round(
            float(score) * 100,
            2
        )

        job["match_percentage"] = match_percentage

        recommendations.append(job)

    recommendations.sort(
        key=lambda job: job["match_percentage"],
        reverse=True
    )

    return recommendations[:top_n]