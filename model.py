from textblob import TextBlob

def predict_sentiment(text: str):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity  # range: [-1, 1]

    if score > 0:
        sentiment = "Bullish"
    elif score < 0:
        sentiment = "Bearish"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "confidence": round(abs(score), 2)
    }