from flask import Flask, render_template, request

from config import project_id
from utils import detect_intent

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    bot_response = detect_intent(project_id, user_input)
    return bot_response


if __name__=='__main__':
    app.run(debug=True, port=5005)
