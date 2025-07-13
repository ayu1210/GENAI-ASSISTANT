Smart Assistant for Research Summarization

An AI-powered web application that enables users to:
 📋 Upload a research document (PDF)
 🧠 Get an automatic summary
 💬 Ask intelligent questions based on document content
 ❓ Practice with challenge-based questions

 Setup Instructions (Step-by-Step)

1. **Clone the repository**

   bash
   git clone https://github.com/<your-username>/smart-assistant.git
   cd smart-assistant

   Create and activate a virtual environment

2. **On Windows**:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate

3. Install dependencies

If you have a requirements.txt:
pip install -r requirements.txt
Otherwise, install manually:

pip install fastapi uvicorn streamlit pdfplumber transformers sentence-transformers streamlit-lottie
4. Start the backend server
cd backend
uvicorn main:app --reload --port 

5.Start the frontend (Streamlit)

Open a new terminal, then run:
cd frontend
streamlit run app.py

6. Open in browser
Frontend: http://localhost:8501
Backend API Docs: http://127.0.0.1:7860/docs

**Architecture & Flow**

User uploads a PDF via the Streamlit frontend
Frontend sends the file to FastAPI backend
Backend extracts text and:
Generates summary using HuggingFace model
Answers questions using context chunking + Q&A pipeline
Provides logic-based challenge questions
Results are displayed live in the browser

**Folder Structure**

smart-assistant/
├── backend/
│   ├── main.py
│   └── utils/
│       ├── summarizer.py
│       ├── qa_engine.py
│       └── question_generator.py
│
├── frontend/
│   ├── app.py
│   └── summary.json (optional Lottie animation)
│
├── sample_docs/
├── requirements.txt
└── README.md







