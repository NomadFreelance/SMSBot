#from twilio.rest import TwilioRestClient
import os
import sys

from flask import Flask, request, redirect
import twilio.twiml

from plugins.util.plugin import plugin_loader

sys.path += ['plugins']

##

class SMSBot(object):
    pass

smsbot = SMSBot()

#### Load plugins

smsbot.commands = {}
command_handler = plugin_loader()

app = Flask(__name__)


@app.route("/hello", methods=['GET', 'POST'])
def hello_world():
    resp = twilio.twiml.Response()
    resp.sms("hello there")
    return str(resp)


@app.route("/", methods=["POST"])
def command():
    text = request.values.get('Body', None)
    if " " in text:
        command, arg = text[1:].split(" ", 1)
    else:
        command = text
        arg = None

    result = command_handler.run(command, arg)
    resp = twilio.twiml.Response()
    resp.sms(result)

    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#client = TwilioRestClient(config.SID, config.TOKEN)
