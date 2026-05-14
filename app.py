from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os

from roast_engine import generate_roast

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text_from_pdf(pdf_path):
    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


@app.route("/", methods=["GET", "POST"])
def index():
    roasts = []

    if request.method == "POST":
        file = request.files["resume"]

        if file:
            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            text = extract_text_from_pdf(filepath)

            roasts = generate_roast(text)

    return render_template("index.html", roasts=roasts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)