import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        year = int(request.form["year"])
        present_price = float(request.form["present_price"])
        kms_driven = int(request.form["kms_driven"])
        fuel_type = int(request.form["fuel_type"])
        seller_type = int(request.form["seller_type"])
        transmission = int(request.form["transmission"])
        owner = int(request.form["owner"])

        prediction = model.predict([[year, present_price, kms_driven,
                                     fuel_type, seller_type,
                                     transmission, owner]])

        output = round(prediction[0], 2)

        return render_template("index.html",
                               prediction_text=f"Predicted Price: ₹ {output} Lakhs")

    except:
        return render_template("index.html",
                               prediction_text="Error in input!")

if __name__ == "__main__":
    app.run(debug=True)
