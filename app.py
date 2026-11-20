import streamlit as st
from src.youtube_utils import get_video_transcript
from src.ai_engine import generate_repurposed_content

st.set_page_config(
    page_title="AI Content Repurposer",
    page_icon="🚀",
    layout="wide"
)

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Content Settings")
    tone = st.selectbox(
        "Content Tone Chunein:",
        ["Engaging & Professional", "Casual & Conversational", "Storytelling", "Bold & Viral"]
    )
    language = st.selectbox(
        "Output Language Chunein:",
        ["English", "Hinglish"]
    )
    st.markdown("---")
    st.info("💡 **Note:** Cloud hosting par kabhi-kabhi YouTube IP block karta hai. Aisi situation me aap **'Paste Text / Transcript'** option use karke turant content bana sakte hain!")

# Main Header
st.title("🚀 AI Content Repurposer")
st.markdown("Kisi bhi **YouTube Video** ya **Article/Script** ko ek click me **LinkedIn Post**, **Twitter/X Thread**, aur **SEO Blog** me badlein.")

# Input Mode Selector
input_mode = st.radio(
    "Input Source Chunein:",
    ["🔗 YouTube Video Link", "📝 Paste Transcript / Article Text"],
    horizontal=True
)

transcript = ""

if input_mode == "🔗 YouTube Video Link":
    video_url = st.text_input(
        "YouTube Video Link Yahan Paste Karein:",
        placeholder="https://www.youtube.com/watch?v=..."
    )
else:
    manual_text = st.text_area(
        "Apna Video Transcript, Notes, ya Article Text Yahan Paste Karein:",
        height=200,
        placeholder="Yahan koi bhi text ya video ki script paste karein..."
    )

# Generate Button
if st.button("✨ Generate Content", type="primary"):
    try:
        if input_mode == "🔗 YouTube Video Link":
            if not video_url.strip():
                st.warning("⚠️ Kripya pehle ek valid YouTube URL paste karein!")
                st.stop()
            with st.spinner("📥 YouTube video se transcript nikala ja raha hai..."):
                transcript = get_video_transcript(video_url)
        else:
            if not manual_text.strip():
                st.warning("⚠️ Kripya pehle kuch text paste karein!")
                st.stop()
            transcript = manual_text.strip()

        # Gemini / Groq AI se Content Generate Karna
        with st.spinner("🧠 AI aapke liye posts likh raha hai..."):
            result = generate_repurposed_content(transcript, tone=tone, language=language)

        st.success("✅ Aapka content taiyar hai!")

        # Clean Tabs me Result Dikhana
        tab1, tab2, tab3, tab4 = st.tabs([
            "💼 LinkedIn Post", 
            "🐦 Twitter / X Thread", 
            "📝 SEO Blog", 
            "📄 Source Text"
        ])

        with tab1:
            st.subheader("Ready-to-Post LinkedIn Content")
            if result["linkedin"]:
                st.markdown(result["linkedin"])
                st.code(result["linkedin"], language="markdown")
            else:
                st.write(result["raw"])

        with tab2:
            st.subheader("Viral Twitter / X Thread")
            if result["twitter"]:
                st.markdown(result["twitter"])
                st.code(result["twitter"], language="markdown")

        with tab3:
            st.subheader("Detailed Blog Article")
            if result["blog"]:
                st.markdown(result["blog"])
                st.download_button(
                    label="📥 Blog Download Karein (.md)",
                    data=result["blog"],
                    file_name="ai_generated_blog.md",
                    mime="text/markdown"
                )

        with tab4:
            st.subheader("Source Text Used")
            st.text_area("Text:", transcript, height=250)

    except Exception as e:
        error_msg = str(e)
        if "blocking requests" in error_msg or "IpBlocked" in error_msg or "RequestBlocked" in error_msg:
            st.error("⚠️ YouTube ne cloud server ke IP ko temporarily block kiya hai. Kripya upar **'📝 Paste Transcript / Article Text'** option select karke video ka transcript ya article paste karein—AI turant content bana dega!")
        else:
            st.error(f"❌ Error: {error_msg}")
