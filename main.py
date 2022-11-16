from flask import Flask, render_template, request
# from jinja2 import markupsafe.escape
# from werkzeug.utils import escape
from markupsafe import Markup, escape

app = Flask(__name__, template_folder='template/')

answer = ""

def validate(uname):
    result = False
    clean = escape(uname)
    if clean == uname:
        result = True
    else: 
        result = False
    return clean, result

@app.route('/', methods=["POST", "GET"])
def main():
    global answer
    if request.method=="POST":
        uname = request.form.get("username")
        clean, is_valid = validate(uname)
        if is_valid:
            answer = clean
            return render_template("result.html", clean=clean)

    return render_template("home.html")

@app.route('/result', methods=["POST", "GET"])
def result():
    global answer
    return render_template("result.html", clean=answer)


def test_add(a_var, b_var):
    return a_var + b_var

def setup():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    setup()
