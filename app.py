from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sentiment
from database import save_result

app = FastAPI(title="Financial Sentiment API")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "API Running"}

@app.post("/predict")
def predict(request: TextRequest):
    result = predict_sentiment(request.text)

    save_result(
        request.text,
        result["sentiment"],
        result["confidence"]
    )

    return result