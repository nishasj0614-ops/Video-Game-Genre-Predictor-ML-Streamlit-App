# Video-Game-Genre-Predictor-ML-Streamlit-App
Predict the genre of a video game using machine learning! 🚀 This interactive Streamlit web app takes inputs like platform, publisher, release year, and regional sales (NA, EU, JP, Other) and predicts the most likely game genre.
🎮 Video Game Genre Predictor

Predict Video Game Genres with Machine Learning and Streamlit!

🔹 Overview

This interactive Streamlit app predicts the genre of a video game based on:

Platform (e.g., Wii, PS4)

Publisher (e.g., Nintendo, EA)

Release Year

Regional sales (NA, EU, JP, Other)

It uses a pre-trained Random Forest model to deliver accurate predictions with a modern dark-themed UI.

⚡ Features

Interactive input forms for game details.

Stylish dark-mode interface.

Instant genre prediction with highlighted results.

Easy-to-use for game analytics and ML enthusiasts.

🖥️ Demo
<p align="center"> <img src="demo_screenshot.png" alt="App Screenshot" width="600"> </p>
🛠️ Installation

Clone the repository:

git clone https://github.com/your-username/video-game-genre-predictor.git
cd video-game-genre-predictor


(Optional) Create a virtual environment:

python -m venv venv
# Activate the environment:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Ensure the trained model best_vgsales_model.joblib is in the root folder.

🚀 Run the App
streamlit run app.py


Open the browser link provided by Streamlit to access the app.

📦 File Structure
video-game-genre-predictor/
│
├─ app.py                      # Streamlit application
├─ best_vgsales_model.joblib    # Pre-trained ML model
├─ requirements.txt            # Python dependencies
├─ README.md                   # Project documentation
└─ demo_screenshot.png         # Optional demo screenshot

🧠 Model Details

Algorithm: Random Forest Classifier

Input Features: Platform, Publisher, Year, NA/EU/JP/Other Sales

Output: Game Genre

💡 Future Improvements

Add more platforms and publishers dynamically.

Include additional sales regions and game metrics.

Deploy publicly on Streamlit Cloud or Heroku.

❤️ Built With

Python

Streamlit

Pandas

Scikit-learn
