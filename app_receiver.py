from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def receiver():
    return render_template("receiver.html")

app.run(debug=True, host='0.0.0.0', port=5501)
