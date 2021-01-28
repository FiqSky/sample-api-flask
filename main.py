import json
import time

from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Success loaded the home page', 'Timestamp': time.time()}
    json_dumps = json.dumps(data_set)

    return json_dumps


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))  # /user/?user=USER_NAME

    data_set = {'Page': 'Request', 'Message': f'Success loaded the request page for {user_query}',
                'Timestamp': time.time()}
    json_dumps = json.dumps(data_set)

    return json_dumps


if __name__ == '__main__':
    app.run(port=3983)
