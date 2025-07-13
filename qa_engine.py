from transformers import pipeline
import pdfplumber

qa = pipeline("question-answering")

def extract_text(content):
    with open("temp.pdf", "wb") as f:
        f.write(content)
    with pdfplumber.open("temp.pdf") as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def chunk_text(text, chunk_size=800):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def answer_question(content, question):
    text = extract_text(content)
    chunks = chunk_text(text)

    best_answer = None
    best_score = 0
    best_context = ""

    for chunk in chunks:
        try:
            result = qa(question=question, context=chunk)
            if result["score"] > best_score:
                best_score = result["score"]
                best_answer = result["answer"]
                best_context = chunk
        except Exception as e:
            print("Error processing chunk:", e)

    justification = f"This answer is supported by: \"{best_context[:250]}...\""
    return best_answer, justification
