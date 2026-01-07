def video_summary_prompt(transcript: str) -> str:
    return f"""
You are an expert AI video summarizer.

Deliver the output in this structure:

### TL;DR
(3 lines max)

### Key Points
- Bullet points

### Insights
- Actionable takeaways

### Final Summary
Concise paragraph

Transcript:
{transcript}
"""
