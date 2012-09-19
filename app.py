#from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml

import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.sms("hello there")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ["PORT"]))

#client = TwilioRestClient(config.SID, config.TOKEN)
