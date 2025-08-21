# 📰 Truth Checker AI

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An AI-based tool that detects whether a news 
article/headline is Real or Fake, using 
Machine Learning (Logistic Regression + TF-IDF).

## Features
- Reads dataset of news headlines/articles (.csv)
- Cleans and preprocesses text (stopwords removal, tokenization)
- Classifies input text as Real News ✅ or Fake News ❌
- Pre-trained model saved in models/ for reuse
- Modular code: train_model.py (training) and main.py (prediction)

## Tech Stack
- Python 3.10
- Pandas, NumPy, Scikit-learn
- NLTK (Natural Language Toolkit)
- Joblib (model persistence)
- Git & GitHub for version control

## Project Structure
```markdown
truth-checker-ai/

├── 📂 dataset/            # CSV dataset of news
├── 📂 models/             # Saved ML model & vectorizer
├── 📂 src/                # Core scripts
│   ├── 🧠 train_model.py  # Train and save your model
│   └── 🎯 main.py         # Predict news authenticity
├── 📄 requirements.txt    # Project dependencies
└── 📘 README.md           # Project overview and instructions
```

## How to Run

### 1. Clone the repository & set up a virtual environment

```bash

git clone https://github.com/anoodh-ai/truth-checker-ai.git
cd truth-checker-ai
python -m venv .venv
.venv\Scripts\activate   # For Windows
#.venv/bin/activate      # For Mac/Linux
pip install -r requirements.txt
```
### 2. Train the model (if needed)
```bash

python src/train_model.py
```
### 3. Add resumes & run the screening
```bash

python src/main.py
```
## Example Output
```bash
Enter news text: Gwen Stefani Got Dumped by Blake Shelton Over "Jealousy and Drama"
✅ Real News

Enter news text: Kandi Burruss Explodes Over Rape Accusation on 'Real Housewives of Atlanta' Reunion (Video)
❌ Fake News

```
## Accuracy

- (Current test dataset) : ~83%
- Expected real-world accuracy: ~75–85% (will improve with larger datasets)

## Future Improvements

- Support for multiple languages
- API or Web UI (Flask/Streamlit)
- Deep Learning models (LSTMs / Transformers)
- Continuous learning from live news feeds

---
 #### 📄 License
```markdown
MIT License — see [LICENSE](LICENSE) for full details.
> This project is shared for learning and inspiration. Please credit the author (Anoodh A) if reused or modified.
```
