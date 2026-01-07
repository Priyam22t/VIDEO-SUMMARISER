import streamlit as st

def set_page():
    st.set_page_config(
        page_title="AI Video Summariser",
        page_icon="🎬",
        layout="wide"
    )

def header():
    st.markdown("# 🎬 AI Video Summariser")
    st.caption("100% Local • No API • No Quota")
