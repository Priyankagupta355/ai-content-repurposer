import streamlit as st
from src.youtube_utils import get_video_transcript
from src.ai_engine import generate_repurposed_content

# Page Configuration (Browser tab ka naam aur icon)
st.set_page_config(
    page_title="AI Content Repurposer",
    page_icon="🚀",
    layout="wide"
)

# Sidebar Settings (Customization Options)
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
    st.info("💡 **Tip:** Kisi bhi YouTube video ka link daalein jisme captions (CC) on hon, aur 10 second me apna social media content taiyar payein!")

# Main Header
st.title("🚀 AI Content Repurposer")
st.markdown("Kisi bhi **YouTube Video** ko ek click me **LinkedIn Post**, **Twitter/X Thread**, aur **SEO Blog** me badlein.")

# User Input Box
video_url = st.text_input(
    "🔗 YouTube Video Link Yahan Paste Karein:",
    placeholder="https://youtube.com..."
)

# Generate Button
if st.button("✨ Generate Content", type="primary"):
    if not video_url.strip():
        st.warning("⚠️ Kripya pehle ek valid YouTube URL paste karein!")
    else:
        try:
            # Step 1: Transcript Fetch Karna
            with st.spinner("📥 YouTube video se transcript nikala ja raha hai..."):
                transcript = get_video_transcript(video_url)

            # Step 2: Gemini AI se Content Generate Karna
            with st.spinner("🧠 Gemini AI aapke liye posts likh raha hai..."):
                result = generate_repurposed_content(transcript, tone=tone, language=language)

            st.success("✅ Aapka content taiyar hai!")

            # Step 3: Clean Tabs me Result Dikhana
            tab1, tab2, tab3, tab4 = st.tabs([
                "💼 LinkedIn Post", 
                "🐦 Twitter / X Thread", 
                "📝 SEO Blog", 
                "📄 Original Transcript"
            ])

            with tab1:
                st.subheader("Ready-to-Post LinkedIn Content")
                if result["linkedin"]:
                    st.markdown(result["linkedin"])
                    st.code(result["linkedin"], language="markdown") # Easy copy button ke liye
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
                st.subheader("Extracted Video Transcript")
                st.text_area("Raw Text:", transcript, height=300)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
