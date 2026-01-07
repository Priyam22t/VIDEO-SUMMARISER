# 🎥 AI Video Summariser (Offline)

AI Video Summariser is a fully offline video transcription and summarization application built using Streamlit, OpenAI Whisper, and Hugging Face Transformers. It allows users to upload video files, convert speech to text locally, and generate concise summaries without using any external APIs or paid services.

---

## ✨ Features

- 📤 Upload video files (MP4, MKV, MOV, MPEG4)
- 📝 Offline speech-to-text transcription using OpenAI Whisper
- 🧠 Local text summarization using Hugging Face Transformers
- ⚡ Clean and simple Streamlit user interface
- 🔒 No API keys, no quotas, no cloud dependency

---

## 🏗️ Project Structure

```
Video-Summariser/
│
├── app.py
├── requirements.txt
│
├── core/
│   └── summarizer.py
│
├── utils/
│   └── whisper_transcribe.py
│
├── assets/
│   └── styles.css
```

---

## 🚀 How It Works

1. User uploads a video file  
2. Whisper transcribes the audio locally  
3. Transcript is passed to a summarization model  
4. A concise summary is generated and displayed  

---

## 🧪 Technologies Used

- Python  
- Streamlit  
- OpenAI Whisper  
- Hugging Face Transformers  
- PyTorch  
- FFmpeg  

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-video-summariser.git
cd ai-video-summariser
```

### 2️⃣ Create and activate environment (recommended)

```bash
conda create -n video_summariser python=3.10
conda activate video_summariser
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

⚠️ First run will download required models (~1–2GB).

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## ⚠️ Known Limitations

- Transcribing long videos may take time  
- Very long transcripts may require chunking  
- YouTube link summarization is not enabled in this version  

---

## 🛠️ Future Improvements

- Automatic chunking for long transcripts  
- YouTube video support via local download  
- Export summaries as PDF or TXT  
- Progress indicators and timestamps  
- Chapter-wise summaries  

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

- OpenAI Whisper  
- Hugging Face Transformers  
- Streamlit  
