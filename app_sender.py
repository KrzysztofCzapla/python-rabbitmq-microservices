from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def sender():
    return render_template("sender.html")

app.run(debug=True, host='0.0.0.0', port=5500)
