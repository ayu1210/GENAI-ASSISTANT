import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Smart Research Assistant", page_icon="📄", layout="wide")

# Load a Lottie animation from a URL or local file
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Optionally include a Lottie animation at the top (place `summary.json` in frontend/ directory)
# Uncomment the following lines if you have a Lottie animation file
# lottie_summary = load_lottie_file("summary.json")
# st_lottie(lottie_summary, height=200, key="summary")

st.title("📚 Smart Assistant for Research Summarization")
st.markdown("""
Welcome to your AI-powered research companion! 🚀 Upload a PDF or TXT document to get:
- 📋 An auto-generated summary
- 💬 Instant Q&A based on the document
- 🧠 Challenge questions for practice
""")

st.markdown("---")

uploaded_file = st.file_uploader("📂 Upload a PDF file", type=["pdf", "txt"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    try:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:7860/upload/", files=files)

        if response.status_code != 200:
            st.error("⚠️ Backend error occurred. Please check logs.")
        else:
            result = response.json()

            if "error" in result:
                st.error("❌ " + result["error"])
            else:
                st.subheader("📋 Auto Summary")
                st.markdown(f"""
                <div style='background-color:#f0f2f6;padding:1.5rem;border-radius:10px;'>
                    {result['summary']}
                </div>
                """, unsafe_allow_html=True)

                mode = st.radio("🤖 Choose Mode:", ["Ask Anything", "Challenge Me"], horizontal=True)

                if mode == "Ask Anything":
                    question = st.text_input("❓ Ask your question:")
                    if question:
                        res = requests.post("http://127.0.0.1:7860/ask/", files=files, data={"question": question})
                        data = res.json()
                        if "error" in data:
                            st.error("❌ " + data["error"])
                        else:
                            st.success("💬 Answer: " + data["answer"])
                            st.caption("📌 " + data["justification"])

                elif mode == "Challenge Me":
                    res = requests.post("http://127.0.0.1:7860/challenge/", files=files)
                    data = res.json()
                    if "error" in data:
                        st.error("❌ " + data["error"])
                    else:
                        st.subheader("🧠 Try answering the following questions:")
                        for i, q in enumerate(data["questions"]):
                            st.text_input(f"Q{i+1}: {q}", key=f"q{i}")

    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")