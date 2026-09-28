
import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)


ALLOWED_EXTENSIONS = {
    "pdf"
}


# Maximum allowed CV file size: 5 MB
MAX_FILE_SIZE = 5 * 1024 * 1024
