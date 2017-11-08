import mine
from flask import Flask
app = Flask(__name__)

@app.route("/")
def show():
    return mine.base.to_html(classes='x')

if __name__ == "__main__":
    app.run(debug=True)