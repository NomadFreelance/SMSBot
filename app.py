#from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect

import config

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.sms("hello there")
    return str(resp)

if __name == "__main__":
    app.run(debug=True)

#client = TwilioRestClient(config.SID, config.TOKEN)
