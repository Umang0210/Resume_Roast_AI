# Resume Roast AI

Resume Roast AI is a small Flask app that lets you upload a PDF resume and returns sarcastic, rule-based feedback based on the text it finds inside the file.

## What It Does

- Accepts a PDF resume upload from the browser.
- Extracts text with `PyPDF2`.
- Analyzes the resume with simple roast rules in `roast_engine.py`.
- Displays the generated roast cards on the page.

## Project Structure

- `app.py` - Flask app, upload handling, and PDF text extraction.
- `roast_engine.py` - Resume analysis and roast generation logic.
- `templates/index.html` - Single-page UI for uploading resumes and showing results.
- `uploads/` - Temporary storage for uploaded PDFs.
- `Dockerfile` - Container image for running the app.

## Requirements

- Python 3.11 or newer
- `pip`

Dependencies are listed in `requirements.txt`:

- `flask`
- `PyPDF2`
- `gunicorn`

## Run Locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

4. Open `http://localhost:5000` in your browser.

## Run With Docker

Build the image:

```bash
docker build -t resume-roast-ai .
```

Run the container:

```bash
docker run --rm -p 5000:5000 resume-roast-ai
```

Then open `http://localhost:5000`.

## How It Works

The app reads the uploaded PDF, converts the text to lowercase, and checks for things like:

- very short or very long resumes
- buzzword-heavy language
- achievements without metrics
- keyword stuffing in the skills section
- missing GitHub references or experience keywords

If no roast rules match, the app returns a default compliment-with-a-side-of-suspicion message.

## Notes

- Only PDF uploads are supported in the current UI.
- Uploaded files are saved into `uploads/`.
- The app listens on port `5000`.
