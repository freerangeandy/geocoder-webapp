from flask import Flask, render_template, request, send_file
from geocode_script import pandas, geocode_addresses

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global geocoded_csv_path
    if request.method == 'POST':
        csv_file = request.files["csv_file"]
        csv_df = pandas.read_csv(csv_file)
        header = None
        if "Address" in csv_df.columns:
            header = "Address"
        elif "address" in csv_df.columns:
            header = "address"
        else:
            return render_template("index.html", error="Please make sure you have an address column in your CSV file!")
        geocoded_df = geocode_addresses(csv_df, header)
        geocoded_csv_path = "uploads/geocoded_"+csv_file.filename
        geocoded_df.to_csv(geocoded_csv_path)
        return render_template("index.html", table=geocoded_df.to_html(), btn="download.html")

@app.route("/download")
def download():
    return send_file(geocoded_csv_path, as_attachment=True, cache_timeout=0)

if __name__ == '__main__':
    app.debug = True
    app.run()
