import streamlit as st
import google.generativeai as genai

# ---------- CONFIG ----------
st.set_page_config(page_title="AI Career Path Recommender", page_icon="🎯")

@st.cache_resource
def load_model():
    """Load and cache the Gemini model."""
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    return genai.GenerativeModel("models/gemini-2.5-flash-lite")

model = load_model()

# ---------- APP TITLE ----------
st.title("🎓 AI Career Path Recommender using Gemini AI")
st.markdown("Get personalized career guidance powered by Google's Generative AI (Gemini).")

# ---------- INPUT FIELDS ----------
degree = st.text_input("🎓 Enter your degree:")
skills = st.text_area("🧠 List your current skills (comma separated):")
interests = st.text_area("💡 Mention your interests or favorite domains:")
goals = st.text_area("🚀 Describe your career goals (short or long term):")

# ---------- GENERATE RECOMMENDATIONS ----------
if st.button("Generate Career Recommendations"):
    if not degree or not skills or not interests:
        st.warning("⚠️ Please fill in all required fields before generating recommendations.")
    else:
        with st.spinner("Generating your personalized career roadmap... please wait ⏳"):
            prompt = f"""
            You are an expert AI career mentor.
            Based on the user's background, suggest **2 ideal career paths**, **key skills** to learn,
            and **short learning resources** for each. Keep it practical and concise.

            Degree: {degree}
            Skills: {skills}
            Interests: {interests}
            Career Goals: {goals}
            """

            try:
                response = model.generate_content(prompt)
                st.success("✅ Career Recommendations Generated Successfully!")
                st.markdown("---")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"⚠️ Error: {e}")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Developed by **Rishabh Chandel** | Powered by Gemini AI | Zeno Talent Internship Project")
