import os


# Backend folder ka path
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# Uploaded CVs ke liye folder
UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)


# Jobs dataset
JOBS_FILE = os.path.join(
    BASE_DIR,
    "jobs.json"
)


# Allowed file types
ALLOWED_EXTENSIONS = {
    "pdf"
}


# Maximum CV size = 5 MB
MAX_FILE_SIZE = 5 * 1024 * 1024