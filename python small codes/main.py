from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        data = request.form.get("user_data")
        result = f"Processed: {data}" # Call your backend function here
    return f'<form method="post"><input name="user_data"><button type="submit">Go</button></form> {result}'

if __name__ == "__main__":
    app.run(debug=True)
