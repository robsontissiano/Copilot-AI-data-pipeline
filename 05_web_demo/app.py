from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", method=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        result = f"ProcessedL {text.upper()}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
