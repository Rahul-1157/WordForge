import streamlit as st
import requests
import os

# Get the API URL from environment variables
API_URL = os.getenv("API_URL")

st.set_page_config(page_title="WordForge", page_icon="🎨", layout="wide")

st.title("🎨 WordForge: LLM-Powered Blog Generator")
st.markdown("Welcome to WordForge! Enter a prompt below and let the LLM Forge it with words.")

with st.form("prompt_form"):
    prompt = st.text_area("Enter your prompt:", height=150)
    submitted = st.form_submit_button("Generate Blog")

if submitted and prompt:
    with st.spinner("Generating Blog... Please wait."):
        try:
            response = requests.post(f"{API_URL}/generate/", json={"prompt": prompt})
            if response.status_code == 200:
                data = response.json()
                st.success("Blog generated successfully!")
                st.subheader("Generated Blog:")
                st.markdown(f"> {data['generated_text']}")
                st.info(f"**Prompt:** {data['prompt']}")
            else:
                st.error(f"Error: Could not generate Blog. Status code: {response.status_code}")
                st.error(f"Details: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while connecting to the backend: {e}")

st.sidebar.header("Generation History")
try:
    history_response = requests.get(f"{API_URL}/history/")
    if history_response.status_code == 200:
        history = history_response.json()
        if history:
            for item in reversed(history):
                with st.sidebar.expander(f"Prompt: {item['prompt'][:50]}..."):
                    st.write(f"**Generated:** {item['generated_text']}")
                    st.caption(f"Created at: {item['created_at']}")
        else:
            st.sidebar.info("No history yet. Generate some text!")
    else:
        st.sidebar.warning("Could not retrieve history.")
except requests.exceptions.RequestException:
    st.sidebar.error("Could not connect to the backend to get history.")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #121212;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)






