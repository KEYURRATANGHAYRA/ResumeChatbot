import os
import uuid
import logging
import logging.handlers

from flask import Flask, render_template, request

import dialogflow
from google.api_core.exceptions import InvalidArgument

from config import project_id, google_credentials
from utils import detect_intent

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials

app = Flask(__name__)

logger = logging.getLogger('logtest')
logger.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s pid/%(process)d %(message)s')
handler = logging.handlers.RotatingFileHandler('logtest.log', maxBytes=1024 * 1024, backupCount=10)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    logger.info('User: {}'.format(user_input))
    bot_response = detect_intent(project_id, user_input)
    logger.info('Bot: {}'.format(bot_response))
    return bot_response


if __name__=='__main__':
    app.run(debug=True, port=5005)
