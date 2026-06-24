import streamlit as st
import random
from notes_data import notes

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f1117;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #d291ff;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: white;
}

.author {
    text-align: center;
    font-size: 14px;
    color: #bfbfbf;
}

.result-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #1e1e2f;
    color: white;
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎵 AI Music Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Generate unique melodies and export them as MIDI files</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="author">Developed by Darsak PS</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### ✨ Features")

    st.markdown("""
- Pattern-Based Melody Generation
- MIDI File Export
- Interactive Streamlit Interface
- AI-Inspired Music Creation
    """)

with col2:
    st.markdown("### 🎼 Melody Generator")

    melody_length = st.slider(
        "Select Melody Length",
        min_value=5,
        max_value=20,
        value=10
    )

    if st.button("🎵 Generate Music"):

            generated_notes = []

            for _ in range(melody_length):
                generated_notes.append(
                    random.choice(notes)
                )

            melody = " - ".join(generated_notes)

            st.success("Music Generated Successfully!")

            st.subheader("🎼 Generated Melody")

            st.markdown(
                f"<div class='result-box'>{melody}</div>",
                unsafe_allow_html=True
            )

            st.download_button(
                label="📥 Download Melody",
                data=melody,
                file_name="generated_melody.txt",
            mime="text/plain"
        )

st.write("")
st.write("")
st.markdown("---")

st.markdown(
    "<p style='text-align:center;color:#bfbfbf;'>© 2026 Darsak PS | Intelligent Melody Generator</p>",
    unsafe_allow_html=True
)