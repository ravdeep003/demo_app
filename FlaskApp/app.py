from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    name = "John Stuart from the Daily Show"
    name = "CS190"
    return render_template('hello.html', name=name)
    


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9999)



