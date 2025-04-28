from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        electricity = float(request.form["electricity"])
        transportation = float(request.form["transportation"])
        
        # Carbon emission calculation (example values)
        elec_emission = electricity * 0.5
        trans_emission = transportation * 0.3

        # Create pie chart
        labels = ["Electricity", "Transportation"]
        sizes = [elec_emission, trans_emission]
        colors = ["#ff9999", "#66b3ff"]
        explode = (0.1, 0)

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct="%1.1f%%", startangle=140)
        plt.axis("equal")

        # Make sure static folder exists
        os.makedirs("static", exist_ok=True)
        plt.savefig("static/chart.png")
        plt.close()

        return render_template("index.html",
                               chart="static/chart.png",
                               electricity=elec_emission,
                               transportation=trans_emission)

    return render_template("index.html", chart=None)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
