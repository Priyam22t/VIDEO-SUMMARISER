import whisper
import tempfile
import os

# Load model once (cached)
model = whisper.load_model("base")

def transcribe_video(uploaded_file):
    """
    Takes Streamlit uploaded video file
    Returns transcript text
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    try:
        result = model.transcribe(temp_path)
        return result["text"]
    finally:
        os.remove(temp_path)
