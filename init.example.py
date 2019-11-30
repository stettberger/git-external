class EchoExtension:
    def cmd_echo(self, args):
        print(args)

    def echo(self, subparser):
        subparser.set_defaults(func=self.cmd_echo)
        subparser.add_argument("-v", "--verbose", help="be verbose",
                               default=False, action="store_true")

    _commands = [('echo', 'Help for echo', echo)]
