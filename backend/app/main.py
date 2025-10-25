from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
import google.generativeai as genai
import os

# Initialize FastAPI app
app = FastAPI(title="WordForge API")

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("No GEMINI_API_KEY found in environment variables.")
genai.configure(api_key=GEMINI_API_KEY)

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate/", response_model=schemas.TextEntry)
def generate_text(text_input: schemas.TextCreate, db: Session = Depends(get_db)):
    """
    Generates a blog post using the Gemini API based on a topic and saves the entry.
    """
    try:
        # 1. Create a more detailed prompt to request a blog post format
        prompt_for_blog = (
            f"Generate a well-structured and engaging blog post on the topic: '{text_input.prompt}'. "
            "The output should be in Markdown. "
            "The very first line must be the title of the post, formatted as a main heading (e.g., '# My Blog Title')."
        )

        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt_for_blog)
        generated_text = response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text with Gemini: {e}")

    # 4. Create a new database entry using the TextEntry model
    db_text_entry = models.TextEntry(
        prompt=text_input.prompt, generated_text=generated_text
    )
    db.add(db_text_entry)
    db.commit()
    db.refresh(db_text_entry)
    return db_text_entry



@app.get("/history/", response_model=list[schemas.TextEntry])
def get_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieves a list of previously generated text entries.
    """
    text_entries = db.query(models.TextEntry).offset(skip).limit(limit).all()
    return text_entries

@app.get("/")
def read_root():
    return {"message": "Welcome to the WordForge API!"}




