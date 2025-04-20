# import streamlit as st
# from search import search_sutra
# import requests
# import os

# # Add your Hugging Face token here
# HF_TOKEN = os.getenv("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") or "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"

# def ask_huggingface_gpt(prompt):
#     API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
#     headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
#     payload = {
#         "inputs": prompt,
#         "parameters": {"max_new_tokens": 250}
#     }
#     response = requests.post(API_URL, headers=headers, json=payload)
#     response_json = response.json()
    
#     if isinstance(response_json, list):
#         return response_json[0]["generated_text"]
#     elif "error" in response_json:
#         return "⚠️ Error: Rate limit exceeded or model still loading..."
#     else:
#         return "⚠️ Unexpected response."

# # UI
# st.title("🧘 AryaMarga Yoga Chatbot (Free GPT Alt)")
# st.write("Ask a question about yoga, and get wisdom based on spiritual sutras.")

# user_input = st.text_input("Ask your question...")

# if user_input:
#     result = search_sutra(user_input)
    
#     st.subheader("📜 Sutra")
#     st.write(result["sutra"])

#     st.subheader("📚 Source")
#     st.write(result["resources"])

#     st.subheader("🧠 GPT-Free Insight")

#     prompt = f"""
# A user asked: "{user_input}"

# Sutra: {result['sutra']}
# Explanation: {result['explanation']}
# Resources: {result['resources']}

# Respond in 3 parts:
# 1. Simple explanation
# 2. Deeper yogic insight
# 3. Book or teacher suggestion to study more
# """

#     reply = ask_huggingface_gpt(prompt)
#     st.write(reply)
import streamlit as st
from search import search_sutra

st.title("🧘 AryaMarga Yoga Chatbot")
st.write("Ask a question and get a sutra-based spiritual response.")

# Input box
user_input = st.text_input("Ask your question...")

if user_input:
    result = search_sutra(user_input)

    st.subheader("📜 Sutra")
    st.write(result["sutra"])

    st.subheader("💡 Explanation")
    st.write(result["explanation"])

    st.subheader("📚 Where to Learn More")
    st.write(result["resources"])

