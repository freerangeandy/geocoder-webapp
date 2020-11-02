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
        content = pandas.read_csv(csv_file, index_col="ID")

        return render_template("index.html", table="table goes here")

if __name__ == '__main__':
    app.debug = True
    app.run()
