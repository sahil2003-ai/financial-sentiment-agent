import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(
    page_title="Financial Sentiment AI",
    layout="wide",
)

# ---------- CUSTOM STYLING ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.big-title {
    font-size: 36px;
    font-weight: bold;
}
.card {
    padding: 20px;
    border-radius: 10px;
    background-color: #1c1f26;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="big-title">📊 Financial Sentiment Dashboard</div>', unsafe_allow_html=True)
st.write("Analyze market sentiment using AI")

st.divider()

# ---------- INPUT SECTION ----------
col1, col2 = st.columns([2,1])

with col1:
    text = st.text_area("Enter Financial News or Headline")

with col2:
    st.markdown("### Actions")
    analyze_btn = st.button("Analyze Sentiment")
    news_btn = st.button("Fetch Live News")

# ---------- RESULT SECTION ----------
if analyze_btn:
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": text}
            )
            result = res.json()

            sentiment = result["sentiment"]
            confidence = result["confidence"]

            st.divider()
            st.subheader("📈 Analysis Result")

            colA, colB, colC = st.columns(3)

            colA.metric("Sentiment", sentiment)
            colB.metric("Confidence", confidence)

            if sentiment == "Bullish":
                colC.success("📈 Positive Market")
            elif sentiment == "Bearish":
                colC.error("📉 Negative Market")
            else:
                colC.info("⚖️ Neutral Market")

            # Progress bar
            st.progress(int(confidence * 100))

        except:
            st.error("API not running. Start FastAPI first.")

# ---------- LIVE NEWS ----------
if news_btn:
    st.divider()
    st.subheader("📰 Latest Market News")

    try:
        from news import fetch_news
        news_list = fetch_news()

        for news in news_list:
            st.markdown(f"• {news}")

    except:
        st.error("Check API key or internet connection")

# ---------- HISTORY (CSV DATA) ----------
st.divider()
st.subheader("📜 Analysis History")

if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
    st.dataframe(df.tail(10), use_container_width=True)
else:
    st.info("No data yet. Run some predictions first.")