from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Load model
    with open("model.pickle", "rb") as f:
        model = pickle.load(f)

    # Load data
    data = pd.read_excel("ulasan1.xlsx")

    # Prediction
    prediction = model.predict(data["ulasan"])

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
