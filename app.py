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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#client = TwilioRestClient(config.SID, config.TOKEN)
