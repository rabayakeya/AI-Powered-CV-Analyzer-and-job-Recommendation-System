import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from parser import extract_text_from_pdf
from recommender import recommend_jobs


app = Flask(__name__)

CORS(app)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)


def allowed_file(filename):
    """
    Check whether the uploaded file is a PDF.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():

    return jsonify({
        "success": True,
        "message": "CVMatch AI backend is running"
    })


@app.route("/api/analyze", methods=["POST"])
def analyze_cv():

    if "cv" not in request.files:

        return jsonify({
            "success": False,
            "message": "No CV file uploaded."
        }), 400

    file = request.files["cv"]

    if file.filename == "":

        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    if not allowed_file(file.filename):

        return jsonify({
            "success": False,
            "message": "Only PDF files are allowed."
        }), 400

    filename = secure_filename(
        file.filename
    )

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(file_path)

    cv_text = extract_text_from_pdf(
        file_path
    )

    if not cv_text:

        return jsonify({
            "success": False,
            "message": "Could not extract text from the CV."
        }), 400

    recommendations = recommend_jobs(
        cv_text,
        top_n=5
    )

    return jsonify({
        "success": True,
        "message": "CV analysed successfully.",
        "filename": filename,
        "extracted_text": cv_text,
        "recommendations": recommendations
    })


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )