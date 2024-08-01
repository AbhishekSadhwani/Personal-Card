from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# for all the template's flask looks inside the templates folder and for all the static files it looks inside the static folder
# static files include images, videos, css files etc


if __name__ == "__main__":
    app.run(debug=True)
