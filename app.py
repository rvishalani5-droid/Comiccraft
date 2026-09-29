import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ComicCraft", page_icon="🎨", layout="wide")

st.title("🎨 ComicCraft - AI Comic Story Creator")
st.write("Using Gemini Models - One idea to full comic!")

with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key", type="password")
    style = st.selectbox("Comic Style", ["Marvel", "Manga", "Cartoon", "Realistic"])
    panels = st.slider("Panels", 3, 8, 4)

prompt = st.text_area("Your Story Idea:", placeholder="A small robot wants to be a chef in space...")

if st.button("Generate Comic 🚀", type="primary"):
    if not api_key:
        st.error("API Key enter pannu da!")
    elif not prompt:
        st.error("Story Idea sollu da!")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        with st.spinner("Creating your comic..."):
            q = f"Create a comic story for '{prompt}' in {style} style with {panels} panels. For each panel give Scene, Dialogue, Narration. Make it fun."
            res = model.generate_content(q)
            st.success("Comic Ready! 🎉")
            st.markdown(res.text)
