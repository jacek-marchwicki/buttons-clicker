from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import my_exceptions
from model import buttons
from firebase import firebase

authentication = firebase.FirebaseAuthentication('ptFwVEJyCHqLobNFlf4Z7dCMBeYDBWKcfsJeyp5p',
                                                  'jacek.marchwicki@gmail.com')
db = firebase.FirebaseApplication('https://amber-heat-6428.firebaseio.com', authentication=authentication)
app = Flask(__name__)


@app.route('/')
def hello_world():
    button1 = buttons.Clicks.get_by_button(1).count
    button2 = buttons.Clicks.get_by_button(2).count
    button3 = buttons.Clicks.get_by_button(3).count
    return render_template('index.html',
                           button1=button1,
                           button2=button2,
                           button3=button3)


@app.route('/api/clicks', methods=['POST'])
def index():
    validate_if_json()
    button = get_int_or_raise("button", my_exceptions.JsonException("No button filed"))
    clicks = buttons.Clicks.get_by_button(button)
    clicks.increment()
    clicks.put()
    buttons.Click(button=button).put()
    db.put("/clicks/", "%d" % button, {"clicks": clicks.count})
    return jsonify({
        "button": button,
        "clicks": clicks.count
    }), 200


def validate_if_json():
    if request.headers['Content-Type'] != 'application/json':
        raise my_exceptions.JsonException("Not a json")

def get_int_or_raise(key, exception):
    try:
        return int(request.json[key])
    except KeyError:
        raise exception

@app.errorhandler(my_exceptions.JsonException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run()
