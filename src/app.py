from flask import Flask, request, render_template
import joblib

# Flask app initialize
app = Flask(__name__)

# Load trained model
with open("C:/Users/anoodhivi/2025-2026 projects/truth-checker-ai/models/fake_news_model.pkl", "rb") as f:

    # Load trained model and vectorizer
    model = joblib.load("C:/Users/anoodhivi/2025-2026 projects/truth-checker-ai/models/fake_news_model.pkl")
    vectorizer = joblib.load("C:/Users/anoodhivi/2025-2026 projects/truth-checker-ai/models/vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")  # UI page

@app.route("/predict", methods=["GET","POST"])
@app.route("/predict", methods=["POST"])

def predict():
    if request.method == "POST":
        news_text = request.form["news_text"]

        # transform text before prediction
        news_tfidf = vectorizer.transform([news_text])
        prediction = model.predict(news_tfidf)

        result = "Fake News ❌" if prediction[0] == 1 else "Real News ✅"
        return render_template("index.html", prediction=result)

    # If GET request, just show empty form
    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)