from flask import Flask, request, jsonify
from bardapi import Bard, SESSION_HEADERS
import requests

app = Flask(__name__)

print('hi')

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/bard')
def answer_bard():
    token = 'fAhDtXsB23RsVQEznQXen5eGVtcmJS5OKGDOsksgnUj-MYxk8ojmecGd6YI3-_xpHaNOfA.'

    ans = Bard(token=token).get_answer("where is your favorite place?")['content']
    return ans 

@app.route('/bard2')
def answer_bard2():
    token = 'fAi3Mv9PgRy3WezGM10NO19EYu80sgrHTaLCK48SnNA6kTipFXrnvvr8u7R93uOkpmhq1g.'
    session = requests.Session()
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set( "__Secure-1PSIDCC", 'ABTWhQE5jkBLpktb0Q6QFROsF3gqGUkKQ-uvVR1EUeO_nI_N1eeXWOFcdFDOJEupvmbvOAec9A')
    session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBPVxjSttv1Q4lerCVzDvO-vQZKbkKynE8tuSMLt61KGfC9mCHlB0YzmP2TXAunfymEAA")
    session.headers = SESSION_HEADERS
    bard = Bard(session=session)
    ans = bard.get_answer("How is the weather today in seoul?")

    return ans 






def process_data(data):
    # Your function here. For example, let's just return the data as is.
    token = 'fAhDtXsB23RsVQEznQXen5eGVtcmJS5OKGDOsksgnUj-MYxk8ojmecGd6YI3-_xpHaNOfA.'

    ans = Bard(token=token).get_answer(data['prompt'])
    return ans 


@app.route('/api', methods=['POST'])
def api():
    print(request.get_json())
    if request.is_json:
        data = request.get_json()
        result = process_data(data)
        return jsonify(result), 200
    else:
        return "Request was not JSON", 400




#if __name__ == '__main__':
    #app.run(debug=True)
