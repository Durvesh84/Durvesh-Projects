import streamlit as st
from resume_parser import extract_text_from_pdf
from matcher import compute_similarity

# Page settings
st.set_page_config(page_title="Resume Matcher", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #1a237e;
    }
    .subheader {
        font-size: 18px;
        color: #333333;
    }
    .stButton > button {
        background-color: #1a237e;
        color: white;
        border: None;
        padding: 10px 20px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("<div class='title'>Resume vs Job Description Matcher</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Upload your resume and paste the job description to check how well they match.</div><br>", unsafe_allow_html=True)

# Layout with 2 columns
col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Upload a clean, recent resume in PDF format.")

with col2:
    jd_text = st.text_area("Paste Job Description", height=250, help="Copy and paste a job description here.")

# Processing section
if uploaded_resume and jd_text:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
        match_score = compute_similarity(resume_text, jd_text)

        st.markdown("### 🎯 Match Result")
        st.success(f"Your resume matches the job description by **{match_score:.2f}%**.")

        # Feedback message
        if match_score < 60:
            st.warning("This is a low match. Try including relevant skills and experiences mentioned in the job description.")
        elif match_score < 80:
            st.info("Good match! A few improvements could still boost your chances.")
        else:
            st.success("Great match! Your resume aligns well with the job description.")

# Footer
st.markdown("---")
st.markdown("Made by Durvesh Chaudhari | Powered by NLP and Streamlit", unsafe_allow_html=True)
