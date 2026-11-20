import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url: str) -> str | None:
    """
    YouTube ke kisi bhi format ke link (laptop, mobile, shorts) me se 
    11-character ki Video ID bahar nikalta hai.
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_video_transcript(video_url: str) -> str:
    """
    Video URL leta hai, ID nikalta hai, aur YouTube se captions fetch karke
    ek clean paragraph me return karta hai.
    """
    video_id = extract_video_id(video_url)
    
    if not video_id:
        raise ValueError("Invalid YouTube URL! Kripya sahi link paste karein.")

    try:
        # Naye version (v1.0+) ka updated tarika
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'hi'])
        
        # Saare text snippets ko space ke saath jodna
        full_transcript = " ".join([snippet.text for snippet in fetched_transcript])
        return full_transcript

    except TranscriptsDisabled:
        raise Exception("Is video ke captions (subtitles) creator ne band kar rakhe hain.")
    except NoTranscriptFound:
        raise Exception("Is video ke liye English ya Hindi captions available nahi hain.")
    except Exception as e:
        raise Exception(f"Transcript nikalne me error aaya: {str(e)}")
