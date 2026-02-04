from fastapi import FastAPI, HTTPException
from models import ChatRequest
from ai_service import generate_ai_answer


app = FastAPI(title="Snowflake GenAI API")


@app.get("/")
def home():
    return {"status": "Running"}


@app.post("/ai-chat")
def ai_chat(req: ChatRequest):

    try:

        answer = generate_ai_answer(req.question)

        return {
            "question": req.question,
            "answer": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
