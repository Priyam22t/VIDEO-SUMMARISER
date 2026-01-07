from transformers import pipeline

# Load summarizer once
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text, max_length=180, min_length=60):
    """
    Summarize transcript text
    """
    if len(text) < 200:
        return "Text too short to summarize."

    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]
