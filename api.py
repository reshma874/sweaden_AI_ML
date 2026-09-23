from flask import Flask, jsonify,request
import joblib

app = Flask(__name__)

model = joblib.load("reshma.pkl")

@app.route("/")
def my_landing_page():
    return "Welcome to my API"

@app.route("/sridhar")
def my_special_function():
    return "Welcome to my home"

@app.route("/predict",methods=["post"])
def predict():

    data = request.json
    size = data["size"]
    prediction = model.predict([[size]])
    prediction_price = float(prediction[0])

    return jsonify({
        "house_size": size,
        "predicted_price": prediction_price
    })
if __name__ == "__main__":
    app.run()