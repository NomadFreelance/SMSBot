SMSBot is an IRC bot for SMS. It's made with Python and the Flask microframework, and replies to SMSes POSTed to it by Twilio.

It uses the plugin architecture I cannibalized from my Shootmania server script project, as well as some code borrowed/repurposed/stolen from Skybot, a popular open source IRC bot. 

All it does is respond to commands defined by plugins, which can have arguments.