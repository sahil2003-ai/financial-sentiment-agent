# 📊 Financial Sentiment Analysis System

A lightweight AI-powered financial sentiment analysis system that analyzes financial news and predicts market sentiment in real-time.

---

## 🚀 Overview

This project is designed to simulate a real-world fintech analytics tool that:

* Analyzes financial text (news, headlines, etc.)
* Predicts sentiment: **Bullish / Bearish / Neutral**
* Displays results through an interactive dashboard
* Stores historical predictions for analysis

Built with performance optimization in mind, this system runs efficiently on low-resource machines.

---

## ✨ Features

* 🔍 Sentiment Analysis (TextBlob-based NLP)
* ⚡ FastAPI backend for real-time predictions
* 🎨 Streamlit dashboard (modern UI)
* 📰 Live financial news integration (NewsAPI)
* 📜 CSV-based data storage (lightweight alternative to database)
* 💻 Optimized for low-end systems (no heavy ML models)

---

## 🧠 Tech Stack

* **Language:** Python
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **NLP:** TextBlob
* **Data Handling:** Pandas, CSV
* **API Integration:** NewsAPI

---

## 📂 Project Structure

```
financial-sentiment-agent/
│
├── app.py              # FastAPI backend
├── model.py            # Sentiment logic
├── dashboard.py        # Streamlit UI
├── news.py             # News API integration
├── database.py         # CSV storage logic
├── requirements.txt    # Dependencies
├── .env.example        # API key template
├── .gitignore          # Ignored files
├── README.md           # Project documentation
└── screenshots/
    ├── dashboard.png
    └── api.png
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/financial-sentiment-agent.git
cd financial-sentiment-agent
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
python -m textblob.download_corpora
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root folder:

```
NEWS_API_KEY=your_api_key_here
```

Get your API key from: https://newsapi.org

---

### 5️⃣ Run FastAPI Backend

```
uvicorn app:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Run Streamlit Dashboard

```
streamlit run dashboard.py
```

---

## 🧪 Example Usage

### Input

```
Company reports strong profit growth
```

### Output

```
Sentiment: Bullish  
Confidence: 0.65
```

---

## 📸 Screenshots

### 📊 Dashboard



### ⚡ API Docs



---

## 🧠 How It Works

1. User inputs financial text
2. FastAPI sends text to sentiment model
3. TextBlob analyzes polarity
4. Sentiment is classified:

   * Positive → Bullish
   * Negative → Bearish
   * Neutral → Neutral
5. Result is displayed in dashboard
6. Data is saved in CSV for history

---

## 💼 Use Cases

* Financial news sentiment tracking
* Market trend analysis
* Demo project for data analyst / data science roles
* Portfolio project for freelancing

---

## 🚀 Future Improvements

* Upgrade to FinBERT (advanced NLP model)
* Add PostgreSQL database (Supabase)
* Deploy API on cloud (Render/AWS)
* Integrate stock price data
* Add charts and analytics dashboard

---

## ⚡ Performance Optimization

This project is specifically optimized for:

* Low RAM systems (8GB)
* CPU-based processing
* Lightweight NLP (no heavy ML models)
* Minimal API calls

---

## 👨‍💻 Author

**Sahil Gaikwad**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!

---
