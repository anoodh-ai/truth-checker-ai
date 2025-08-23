from flask import Flask, render_template, request
import joblib, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'fake_news_model.pkl')
VEC_PATH   = os.path.join(BASE_DIR, '..', 'models', 'vectorizer.pkl')

# load once at startup
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VEC_PATH)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'),
)

def predict_label(text: str):
    x = vectorizer.transform([text])
    pred = int(model.predict(x)[0])           # 1=Real, 0=Fake (as per your training)
    score = None
    if hasattr(model, "predict_proba"):
        score = float(model.predict_proba(x)[0][pred]) * 100.0
    label = "✅ Real News" if pred == 1 else "❌ Fake / Unreliable"
    return label, score

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text", "").strip()
    if not text:
        return render_template("index.html", error="Please paste some news text.")
    label, score = predict_label(text)

    # 🔹 Color logic with warning
    if "Real" in label:
        if score is not None and score < 60:
            color = "warning"  # 🟨 Low confidence real → yellow
        else:
            color = "success"  # 🟩 High confidence real → green
    else:
        if score is not None and score < 60:
            color = "warning"  # 🟨 Low confidence fake → yellow
        else:
            color = "danger"  # 🟥 High confidence fake → red
    return render_template("result.html", label=label, score=score, text=text, color=color)

@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # for local dev only
    app.run(host="127.0.0.1", port=5000, debug=True)