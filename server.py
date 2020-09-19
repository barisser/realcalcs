from flask import Flask
from flask import request, render_template
from flask import make_response
import json
import time
import random


from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

bootstrap = Bootstrap(app)


@app.route('/')
def respond_to_index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def redmatter():
    response=make_response("you just sent a post request, the time is " + str(time.time()), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin']= '*'
    return response


def serve():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
   serve()
