from flask import Flask, render_template, request
import pandas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        csv_file = request.files["csv_file"]
        csv_df = pandas.read_csv(csv_file, index_col="ID")
        if "Address" in csv_df.columns or "address" in csv_df.columns:
            return render_template("index.html", table="table goes here")
        else:
            return render_template("index.html", error="Please make sure you have an address column in your CSV file!")

if __name__ == '__main__':
    app.debug = True
    app.run()
