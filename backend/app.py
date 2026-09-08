import os
import uuid

from flask import (
    Flask,
    request,
    jsonify
)

from flask_cors import CORS

from werkzeug.utils import (
    secure_filename
)

from config import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS,
    MAX_FILE_SIZE
)

from parser import parse_cv

from recommender import (
    recommend_jobs
)


# Flask application
app = Flask(__name__)


# CORS enable
CORS(app)


# Maximum upload size
app.config[
    "MAX_CONTENT_LENGTH"
] = MAX_FILE_SIZE


# Upload folder create karo
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


def allowed_file(filename):
    """
    Check karta hai ke uploaded file
    allowed extension ki hai ya nahi.
    """

    if "." not in filename:
        return False


    extension = filename.rsplit(
        ".",
        1
    )[1].lower()


    return extension in ALLOWED_EXTENSIONS


@app.route(
    "/api/health",
    methods=["GET"]
)
def health_check():
    """
    Backend testing endpoint.
    """

    return jsonify({
        "status": "success",
        "message": "CV Recommendation Backend is running"
    })


@app.route(
    "/api/analyze",
    methods=["POST"]
)
def analyze_cv():
    """
    CV upload aur analysis endpoint.
    """

    # Check CV file
    if "cv" not in request.files:

        return jsonify({
            "status": "error",
            "message": "No CV file provided."
        }), 400


    file = request.files["cv"]


    # Empty filename
    if file.filename == "":

        return jsonify({
            "status": "error",
            "message": "No file selected."
        }), 400


    # Check PDF
    if not allowed_file(
        file.filename
    ):

        return jsonify({
            "status": "error",
            "message": "Only PDF files are allowed."
        }), 400


    # Secure original filename
    original_filename = (
        secure_filename(
            file.filename
        )
    )


    # Unique filename
    unique_filename = (
        str(uuid.uuid4())
        + "_"
        + original_filename
    )


    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )


    try:

        # Save uploaded CV
        file.save(file_path)


        # Parse CV
        parsed_cv = parse_cv(
            file_path
        )


        # Job recommendations
        recommendations = recommend_jobs(
            parsed_cv["text"],
            top_n=5
        )


        # Final response
        response = {

            "status": "success",

            "filename": (
                original_filename
            ),

            "skills": (
                parsed_cv["skills"]
            ),

            "entities": (
                parsed_cv["entities"]
            ),

            "recommendations": (
                recommendations
            )
        }


        return jsonify(
            response
        ), 200


    except ValueError as error:

        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400


    except Exception as error:

        print(
            "Backend Error:",
            error
        )

        return jsonify({
            "status": "error",
            "message": "Internal server error."
        }), 500


    finally:

        # CV ko processing ke baad
        # delete kar do
        if os.path.exists(
            file_path
        ):

            os.remove(
                file_path
            )


@app.errorhandler(413)
def file_too_large(error):

    return jsonify({
        "status": "error",
        "message": "CV file is too large. Maximum size is 5 MB."
    }), 413


@app.errorhandler(404)
def page_not_found(error):

    return jsonify({
        "status": "error",
        "message": "API endpoint not found."
    }), 404


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )