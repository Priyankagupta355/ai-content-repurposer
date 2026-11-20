def get_repurpose_prompt(transcript: str, tone: str = "Engaging & Professional", language: str = "English") -> str:
    """
    YouTube transcript ko LinkedIn post, Twitter thread, aur Blog me badalne ke liye
    structured prompt taiyar karta hai.
    """
    return f"""
    You are an expert Tech Content Creator and Social Media Strategist.
    Analyze the following YouTube video transcript and repurpose it into three high-performing content formats.

    **Rules & Preferences:**
    - Tone: {tone}
    - Output Language: {language} (If Hinglish is selected, write in natural conversational Hindi using English alphabets, just like Indian tech creators).
    - Do not hallucinate facts; stick strictly to the insights from the transcript.

    **Required Outputs:**

    1. **LinkedIn Post:**
       - Start with a strong, scroll-stopping hook (1-2 lines).
       - Use short paragraphs and bullet points for readability.
       - Highlight 3-5 key takeaways from the video.
       - End with an engaging question to drive comments and 3-5 relevant hashtags.

    2. **Twitter / X Thread:**
       - Create a 5 to 6 tweet thread.
       - Tweet 1 must be a killer hook with "🧵👇".
       - Keep every single tweet strictly under 280 characters.
       - Separate each tweet clearly with "---".

    3. **SEO Blog Post:**
       - Catchy H1 Title.
       - Brief Introduction.
       - Well-structured body with H2 subheadings and bullet points.
       - Actionable Conclusion.

    **Format your response strictly with these exact headers so it can be parsed easily:**
    ===LINKEDIN===
    (Write LinkedIn post here)
    ===TWITTER===
    (Write Twitter thread here)
    ===BLOG===
    (Write Blog post here)

    **Video Transcript:**
    {transcript}
    """
