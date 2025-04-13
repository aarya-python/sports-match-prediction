import pickle
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend communication

# ✅ Add a homepage to fix the 404 error
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Sports Prediction API! Use the /predict endpoint to get match predictions."

# ✅ Load the trained model
try:
    model_path = "C:/Users/HP/Desktop/model.pkl"
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# ✅ Load the win ratios
try:
    win_ratios_path = "C:/Users/HP/Desktop/win_ratios.csv"
    win_ratios = pd.read_csv(win_ratios_path)
    win_ratio_dict = win_ratios.set_index("team").to_dict()["win_ratio"]
    print("✅ Win ratios loaded successfully!")
except Exception as e:
    print(f"❌ Error loading win ratio data: {e}")

# ✅ Define the prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Get JSON input from user
        print(f"📥 Received Data: {data}")  # Debugging: Print received data

        # Extract input features
        team1 = data["team1"]
        team2 = data["team2"]
        toss_winner = data["toss_winner"]
        venue = data["venue"]

        # Convert team names to win ratios
        team1_win_ratio = win_ratio_dict.get(team1, 0)
        team2_win_ratio = win_ratio_dict.get(team2, 0)

        # Debugging: Print transformed input data
        print(f"📊 Transformed Data: team1_win_ratio={team1_win_ratio}, team2_win_ratio={team2_win_ratio}")

        # Convert inputs into a DataFrame for prediction
        input_data = pd.DataFrame([[team1_win_ratio, team2_win_ratio]], columns=["team1_win_ratio", "team2_win_ratio"])

        # Make prediction (1 = team1 wins, 0 = team2 wins)
        prediction = model.predict(input_data)[0]
        predicted_winner = team1 if prediction == 1 else team2

        # Debugging: Print prediction result
        print(f"🎯 Prediction: {predicted_winner}")

        return jsonify({"predicted_winner": predicted_winner})  # Return the prediction as JSON
    
    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500  # Return error if something goes wrong

# ✅ Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
