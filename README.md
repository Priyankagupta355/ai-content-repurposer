🌐 **Live Demo:** [ai-content-repurposer-f2fsywcgyerwf8vlf8gdyy.streamlit.app](https://ai-content-repurposer-f2fsywcgyerwf8vlf8gdyy.streamlit.app/)

# 🚀 AI Content Repurposer

An AI-powered web application built with **Python, Streamlit, and Groq LLM API** that transforms any YouTube video into ready-to-publish **LinkedIn Posts, Twitter/X Threads, and SEO Blogs** in seconds.

## ✨ Features

- **Automatic Transcript Extraction:** Fetches English & Hindi captions directly from YouTube URLs.
- **Multi-Platform Output:** Generates formatted LinkedIn posts, 280-char Twitter threads, and structured Markdown blogs in a single click.
- **Customizable Tone & Language:** Supports multiple content tones and both **English** & **Hinglish** outputs.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Engine:** Groq API (`openai/gpt-oss-120b`)
- **Data Extraction:** `youtube-transcript-api`

## ⚙️ Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd ai-content-repurposer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
