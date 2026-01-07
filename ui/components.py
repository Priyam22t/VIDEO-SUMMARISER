import streamlit as st

def input_section():
    with st.container(border=True):
        st.subheader("📥 Input Video / Text")

        youtube_url = st.text_input(
            "YouTube URL (optional)",
            placeholder="https://www.youtube.com/watch?v=..."
        )

        uploaded_file = st.file_uploader(
            "Upload video file (optional)",
            type=["mp4", "mkv", "mov"]
        )

        transcript = st.text_area(
            "Or paste transcript text",
            height=200,
            placeholder="Paste transcript here if you already have it..."
        )

        return youtube_url, uploaded_file, transcript


def summary_box(summary: str):
    with st.container(border=True):
        st.subheader("🧠 Summary")
        st.write(summary)
