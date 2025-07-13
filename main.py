from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from utils.summarizer import generate_summary
from utils.qa_engine import answer_question
from utils.question_generator import generate_questions

app = FastAPI()

# CORS middleware for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test endpoint to confirm it's working
@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    summary = generate_summary(content)
    return {"summary": summary}

@app.post("/ask/")
async def ask_question(file: UploadFile = File(...), question: str = Form(...)):
    content = await file.read()
    answer, justification = answer_question(content, question)
    return {"answer": answer, "justification": justification}

@app.post("/challenge/")
async def challenge_user(file: UploadFile = File(...)):
    content = await file.read()
    questions = generate_questions(content)
    return {"questions": questions}
