import json

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from config import JOBS_FILE


def load_jobs():
    """
    jobs.json se jobs load karta hai.
    """

    with open(
        JOBS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)

    return jobs


def calculate_similarity(
    cv_text,
    jobs
):
    """
    CV aur jobs ke beech
    cosine similarity calculate karta hai.
    """

    documents = [cv_text]

    for job in jobs:

        documents.append(
            job["description"]
        )


    # TF-IDF
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )


    tfidf_matrix = (
        vectorizer.fit_transform(
            documents
        )
    )


    # CV vector
    cv_vector = tfidf_matrix[0:1]


    # Job vectors
    job_vectors = tfidf_matrix[1:]


    # Cosine similarity
    similarities = cosine_similarity(
        cv_vector,
        job_vectors
    )[0]


    return similarities


def recommend_jobs(
    cv_text,
    top_n=5
):
    """
    CV ke liye top matching jobs return karta hai.
    """

    jobs = load_jobs()


    if not jobs:
        return []


    similarities = calculate_similarity(
        cv_text,
        jobs
    )


    recommendations = []


    for index, similarity in enumerate(
        similarities
    ):

        job = jobs[index].copy()


        # Similarity 0-1 hoti hai.
        # Isko percentage mein convert kar rahe hain.
        match_score = (
            float(similarity) * 100
        )


        job["match_score"] = round(
            match_score,
            2
        )


        recommendations.append(job)


    # Highest score first
    recommendations.sort(
        key=lambda job: job["match_score"],
        reverse=True
    )


    # Top N jobs
    return recommendations[:top_n]