import streamlit as st
import google.generativeai as genai
import docx
import os

# 1. API Key کو سسٹم انوائرنمنٹ یا سائیڈ بار سے حاصل کریں
# محفوظ طریقہ: st.secrets کا استعمال کریں
st.set_page_config(page_title="SEO Humanizer Pro", layout="centered")

st.title("✍️ SEO Content Humanizer Pro")
st.markdown("---")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

uploaded_file = st.file_uploader("Upload your file (TXT or DOCX)", type=['txt', 'docx'])

if uploaded_file and api_key and st.button("Humanize Now"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        content = "\n".join([para.text for para in doc.paragraphs])
    else:
        content = uploaded_file.read().decode("utf-8")
    
    with st.spinner('Processing...'):
        prompt = f"Rewrite this content to be 100% human-written, engaging, and SEO-optimized. Content: {content}"
        response = model.generate_content(prompt)
        
        st.write("### ✅ Humanized Result:")
        st.success(response.text)
        
        st.download_button("Download Result", response.text, file_name="humanized_content.txt")
