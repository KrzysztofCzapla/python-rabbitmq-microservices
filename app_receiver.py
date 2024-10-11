from flask import Flask, render_template, request

from receiver.receive import receive

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sender():
    if request.method == "POST":
        return render_template("receiver.html", message=receive())
    return render_template("receiver.html")

app.run(debug=True, host='0.0.0.0', port=5501)
