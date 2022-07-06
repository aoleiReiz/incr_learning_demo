from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config["template_folder"] = "templates"
app.config["static_folder"] = "static"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
