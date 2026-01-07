import streamlit as st
from utils.whisper_transcribe import transcribe_video
from core.summarizer import summarize_text

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Video Summariser",
    page_icon="🎥",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🎥 AI Video Summariser")
st.caption("100% Local • Whisper + Transformers • No API • No Quota")

st.divider()

# ---------------- INPUT ----------------
st.subheader("Input Video")

uploaded_video = st.file_uploader(
    "Upload video file",
    type=["mp4", "mkv", "mov", "mpeg4"]
)

st.divider()

# ---------------- ACTION ----------------
if st.button("✨ Generate Summary", use_container_width=True):

    if not uploaded_video:
        st.error("Please upload a video file.")
        st.stop()

    with st.spinner("📝 Transcribing video (Whisper)..."):
        transcript = transcribe_video(uploaded_video)

    st.subheader("Transcript")
    st.text_area("Extracted Transcript", transcript, height=250)

    with st.spinner("🧠 Generating summary..."):
        summary = summarize_text(transcript)

    st.subheader("Summary")
    st.success(summary)

# ---------------- FOOTER ----------------
with st.expander("🛠 Debug Info"):
    st.write("Video uploaded:", uploaded_video is not None)
