import os
from dotenv import load_dotenv
from groq import Groq
from src.prompts import get_repurpose_prompt

load_dotenv(override=True)

def generate_repurposed_content(transcript: str, tone: str = "Engaging & Professional", language: str = "English") -> dict:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY nahi mili! Kripya apni .env file check karein.")

    client = Groq(api_key=api_key)
    prompt = get_repurpose_prompt(transcript, tone, language)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
        )
        
        raw_text = response.choices[0].message.content

        linkedin_post = ""
        twitter_thread = ""
        blog_post = ""

        if "===LINKEDIN===" in raw_text and "===TWITTER===" in raw_text:
            part1 = raw_text.split("===LINKEDIN===")
            linkedin_post, rest = part1[1].split("===TWITTER===")
            
            if "===BLOG===" in rest:
                twitter_thread, blog_post = rest.split("===BLOG===")
            else:
                twitter_thread = rest

        return {
            "linkedin": linkedin_post.strip(),
            "twitter": twitter_thread.strip(),
            "blog": blog_post.strip(),
            "raw": raw_text
        }

    except Exception as e:
        raise Exception(f"AI se content generate karne me error aaya: {str(e)}")
