from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
data = pd.read_csv("cars.txt")

# Convert categorical data
data['Fuel_Type'] = data['Fuel_Type'].map({'Petrol':0, 'Diesel':1, 'CNG':2})
data['Seller_Type'] = data['Seller_Type'].map({'Dealer':0, 'Individual':1})
data['Transmission'] = data['Transmission'].map({'Manual':0, 'Automatic':1})

# Features and target
X = data[['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
y = data['Selling_Price']

# Train model
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return '''
    <h2>Car Price Prediction</h2>
    <form action="/predict" method="post">
        Year: <input type="text" name="Year"><br>
        Present Price: <input type="text" name="Present_Price"><br>
        Kms Driven: <input type="text" name="Kms_Driven"><br>
        Fuel Type (0=Petrol,1=Diesel,2=CNG): <input type="text" name="Fuel_Type"><br>
        Seller Type (0=Dealer,1=Individual): <input type="text" name="Seller_Type"><br>
        Transmission (0=Manual,1=Automatic): <input type="text" name="Transmission"><br>
        Owner: <input type="text" name="Owner"><br>
        <input type="submit" value="Predict">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]
    prediction = model.predict([input_data])
    return f"<h3>Estimated Car Price: ₹ {round(prediction[0],2)} lakhs</h3>"

if __name__ == "__main__":
    app.run(debug=True)