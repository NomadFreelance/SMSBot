import importlib
from commands import *


class CommandHandler:
    def __init__(self, commands):
        self.commands = commands

    def add(self, *args, **kwargs):
        self.commands[args[0]] = Command(*args, **kwargs)

    def run(self, name, *args):
        name = name.lower()

        if name in self.commands:
            response = self.commands[name].run(*args)
            return response
        else:
            return "Command does not exist."


class Command:
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.function = args[1]
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def run(self, arg):
        if self.has_arg == True:
            if arg == None:
                return "No argument given."
            else:
                args.append(arg)
                response = self.function(arg)
        else:
            response = self.function()
        return response


class Plugin(object):
    def __init__(self):
        self.commands = {}

    def add_command(self, *args, **kwargs):
        self.commands[args[0]] = Command(*args, **kwargs)


# todo: exceptions for missing plugins
def plugin_loader():
    commands = {}
    plugins_config = {"bitcoin": {}}

    for name, config in plugins_config.iteritems():
        Plugin = importlib.import_module("plugins." + name).ExportPlugin
        plugin = Plugin()
        commands = dict(commands.items() + plugin.commands.items())

    return CommandHandler(commands)
