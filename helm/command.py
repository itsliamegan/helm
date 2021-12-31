def command(description, *parameters):
	def wrap(action):
		return Command(action.__name__, description, parameters, action)

	return wrap

class Command:
	def __init__(self, name, description, parameters, action):
		self.name = name
		self.description = description
		self.parameters = parameters
		self.action = action

	def run(self, *args, **kwargs):
		return self.action(*args, **kwargs)

	def define_on(self, parser):
		subparser = parser.add_parser(self.name, help=self.description)

		for parameter in self.parameters:
			parameter.define_on(subparser)
