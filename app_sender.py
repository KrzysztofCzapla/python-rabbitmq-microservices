from flask import Flask, render_template, request

from sender.send import send

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sender():
    if request.method == "POST":
        message = request.form.get('message', "Hello!")
        send(message)
        return render_template("sender.html", message=message)
    return render_template("sender.html")


app.run(debug=True, host='0.0.0.0', port=5500)
