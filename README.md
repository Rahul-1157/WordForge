# WordForge: LLM-Powered Blog Generation

**WordForge** is a full-stack application that leverages the power of Google's **LLM** to generate creative and contextually relevant text.  
The backend is built with **FastAPI** and uses a **PostgreSQL** database, ready for deployment on **Render**.  
The frontend is an interactive **Streamlit** application designed for deployment on **Streamlit Cloud**.


---

## 🚀 Features

- **LLM-Powered Text Generation:** Utilizes the LLM to generate high-quality, context-aware text based on user prompts.  
- **Robust Backend:** A scalable and efficient backend built with FastAPI.  
- **Persistent Storage:** Uses PostgreSQL to store generated content and user history.  
- **Interactive Frontend:** A user-friendly interface created with Streamlit.  
- **Containerized Deployment:** Includes a Dockerfile for easy deployment on Render.  
- **Cloud-Native:** Optimized for cloud platforms like Render and Streamlit Cloud.  

---

## 🛠️ Deployment

### Backend (Render)

1. **Fork this repository.**  
2. **Create a new Web Service** on [Render](https://render.com).  
3. Connect your forked repository.  
4. Set the runtime to **Docker**.  
5. Set the root directory to `./backend`.  
6. Render will automatically detect your `Dockerfile`.  
7. **Add environment variables:**
   - `DATABASE_URL`: Your PostgreSQL connection string from Render’s Postgres addon.  
   - `GEMINI_API_KEY`: Your Gemini API key.  
8. **Deploy!**

---

### Frontend (Streamlit Cloud)

1. **Fork this repository.**  
2. Go to your [Streamlit Cloud dashboard](https://streamlit.io/cloud).  
3. Click **“New app”** and connect your forked repository.  
4. Set:
   - **Branch:** `main`  
   - **File path:** `frontend/streamlit_app.py`  
5. **Add environment variables:**
   - `API_URL`: The URL of your deployed FastAPI backend on Render.  
6. **Deploy!**

---

## 💡 Usage

Once both the **backend** and **frontend** are deployed:

1. Open your **Streamlit app URL**.  
2. Enter a text prompt.  
3. **Chitralekha** will generate a creative and contextually relevant text response for you.

---

## 🧠 Tech Stack

- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **Frontend:** Streamlit  
- **LLM Model:** Google Gemini  
- **Deployment:** Render (backend) & Streamlit Cloud (frontend)  
- **Containerization:** Docker  

---

**Crafted with ❤️ by PAWAN SHARMA.**




