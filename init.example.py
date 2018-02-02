class EchoExtension:
    def __init__(self, commands):
        self.all_commands = commands

    def cmd_echo(self, *args):
        print(args)
        print(self.all_commands)

    def commands(self):
        """An extension class is found by having this attribute. It is
           supposed to return a dict structured like:

           {ARG: (HELP, CMD)}

        """
        return {'echo': (' -- echo everything (from init.example.py)', self.cmd_echo)}
