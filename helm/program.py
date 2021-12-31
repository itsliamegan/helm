from argparse import ArgumentParser

class Program:
	def __init__(self, name, commands):
		parser = ArgumentParser(prog=name)
		subparser = parser.add_subparsers(title="subcommands", dest="command")

		for command in commands:
			command.define_on(subparser)

		self.commands = commands
		self.parser = parser

	def run(self, argv):
		args = self.parser.parse_args(argv)

		for command in self.commands:
			if command.name == args.command:
				values = vars(args)
				del values["command"]

				return command.run(**values)

		self.parser.print_help()
