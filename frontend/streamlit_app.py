import streamlit as st
import requests

st.title("Automated Resume Relevance Check")

uploaded_jd = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Evaluate"):
    if uploaded_jd and uploaded_resume:
        files = {
            "job_description": (uploaded_jd.name, uploaded_jd, "application/pdf"),
            "resume": (uploaded_resume.name, uploaded_resume, "application/pdf")
        }
        response = requests.post("http://127.0.0.1:8000/api/evaluate/", files=files)


        if response.ok:
            data = response.json()
            st.write(f"Relevance Score: {data['score']}")
            st.write(f"Verdict: {data['verdict']}")
            st.write(f"Missing Skills: {', '.join(data['missing_skills']) if data['missing_skills'] else 'None'}")
            st.write("Suggestions:")
            for sugg in data["suggestions"]:
                st.write(f"- {sugg}")
        else:
            st.error(f"Error: {response.text}")
    else:
        st.warning("Please upload both Job Description and Resume")
