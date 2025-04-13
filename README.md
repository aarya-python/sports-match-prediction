# sports-match-prediction
# 🏏 Sports Match Prediction using Machine Learning

This project predicts the outcome of IPL cricket matches based on historical match data, toss decisions, and venue. The model uses logistic regression for classification and provides predictions through a Flask-based web app.

---

 Project Overview

- Developed a machine learning model to predict IPL match winners.
- Integrated match and player data (matches.csv & deliveries.csv) to generate features like team win ratios.
- Built a web-based interface using HTML and Flask to allow users to input match scenarios and get predictions.
- Accuracy achieved: **51%** (baseline model; room for improvements with more complex features and ensemble models).

---

Technologies Used

- Python 3.13  
- Pandas, NumPy, Scikit-learn  
- Flask (for backend API)  
- HTML/CSS (for frontend interface)  
- Matplotlib & Seaborn (for EDA)  
- Git & GitHub (for version control)

---

Model and Features

- **Algorithm used**: Logistic Regression
- **Features**:
  - `team1`, `team2` – Participating teams
  - `toss_winner` – Team that won the toss
  - `venue` – Match location
  - `team1_win_ratio`, `team2_win_ratio` – Historical win percentages

---

How to Run This Project
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/sports-match-prediction.git
   cd sports-match-prediction

   nstall dependencies:
pip install -r requirements.txt

Run the Flask app:
python app.py

Open your browser and go to:
http://127.0.0.1:5000
