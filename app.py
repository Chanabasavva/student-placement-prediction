from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# CREATE FLASK APP (THIS WAS MISSING)
app = Flask(__name__)
CORS(app)

# HOME PAGE
@app.route("/")
def home():
    return render_template("predict.html")

# PREDICT ROUTE
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    cgpa = float(data["cgpa"])
    internships = int(data["internships"])
    skills = int(data["skills"])

    if cgpa >= 6 and internships >= 1 and skills >= 5:
        result = "Placed"
    else:
        result = "Not Placed"

    return jsonify({"prediction": result})

# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)