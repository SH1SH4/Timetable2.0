from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/registration', methods=["POST", "GET"])
def registration():
    if request.method == "GET":
        return render_template('registration.html')
    if request.method == "POST":
        print(request.form.get('password'))
        print(request.form.get('email'))
        print(request.form.get('name'))
        print(request.form.get('surname'))
        return "OK"


@app.route("/authorization", methods=["POST", "GET"])
def authorization():
    if request.method == "GET":
        return render_template('authorization.html')
    if request.method == "POST":
        print(request.form.get('password'))
        print(request.form.get('email'))
        return "OK"


if __name__ == "__main__":
    app.run()