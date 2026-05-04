from fastapi import FastAPI
from models import TextRequest, QARequest, ProcessRequest
from services.ai_service import summarize_text, improve_grammar, answer_question, classify_intent, process_input
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI text-processign API")

@app.post("/summarize")
def summarize(req: TextRequest):
    logger.info("Summarizing text request received")

    try:
        result = summarize_text(req.text)
        return {
        "status": "success",
        "data": {"summary": result}
    }
    except Exception as e:
        logger.error("Failed to process request")
        return {
        "status": "error",
        "message": "Failed to process request"
    }

@app.post("/improve-grammar")
def grammar(req: TextRequest):
    logger.info("Improve grammar request received")
    try:
        result = improve_grammar(req.text)
        return {
        "status": "success",
        "data": {"improved_text": result}
    }
    except Exception as e:
        logger.error("Failed to process request")
        return {
        "status": "error",
        "message": "Failed to process request"
    }


@app.post("/ask")
def ask(req: QARequest ):
   logger.info("QA request received")
   try:
    result = answer_question(req.context, req.question)
    return {
        "status": "success",
        "data": {"answer": result}
    }
   except Exception as e:
        logger.error("Failed to process request")
        return {
        "status": "error",
        "message": "Failed to process request"
    }
    
    
@app.post("/process")
def process(req: ProcessRequest):
    try:
        result = process_input(req.input, req.session_id, req.context)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to process request due to error {str(e)}")
        return {
            "status": "error",
            "message": f"Processing failed with error {str(e)}"
        }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)
