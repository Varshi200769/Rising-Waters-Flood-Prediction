from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model", "floods.save"))
scaler = joblib.load(os.path.join(BASE_DIR, "model", "scaler.save"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    temp = float(request.form["Temp"])
    humidity = float(request.form["Humidity"])
    cloud = float(request.form["Cloud Cover"])
    annual = float(request.form["ANNUAL"])
    janfeb = float(request.form["Jan-Feb"])
    marmay = float(request.form["Mar-May"])
    junsep = float(request.form["Jun-Sep"])
    octdec = float(request.form["Oct-Dec"])
    avgjune = float(request.form["avgjune"])
    sub = float(request.form["sub"])

    values = np.array([[temp,
                        humidity,
                        cloud,
                        annual,
                        janfeb,
                        marmay,
                        junsep,
                        octdec,
                        avgjune,
                        sub]])

    scaled = scaler.transform(values)

    prediction = model.predict(scaled)

    if prediction[0] == 1:
        return render_template("flood.html")

    return render_template("noflood.html")


if __name__ == "__main__":
    app.run(debug=True)