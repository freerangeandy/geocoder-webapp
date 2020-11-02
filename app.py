from flask import Flask, render_template, request
from geocode_script import pandas, geocode_addresses

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        csv_file = request.files["csv_file"]
        csv_df = pandas.read_csv(csv_file, index_col="ID")
        header = None
        if "Address" in csv_df.columns:
            header = "Address"
        elif "address" in csv_df.columns:
            header = "address"
        else:
            return render_template("index.html", error="Please make sure you have an address column in your CSV file!")

        geocoded_df = geocode_addresses(csv_df, header)
        return render_template("index.html", table=geocoded_df.to_numpy(), headers=geocoded_df.columns)

if __name__ == '__main__':
    app.debug = True
    app.run()
