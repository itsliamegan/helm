def argument(name, description, type=str, default=None):
	return Argument(name, description, type, default)

def option(name, description, type=str, default=None):
	return Option(name, description, type, default)

def flag(name, description):
	return Flag(name, description)

class Argument:
	def __init__(self, name, description, type, default):
		self.name = name
		self.description = description
		self.type = type
		self.default = default
		self.required = default is None

	def define_on(self, parser):
		if self.required:
			parser.add_argument(
				self.name,
				help=self.description,
				type=self.type
			)
		else:
			parser.add_argument(
				self.name,
				help=self.description,
				type=self.type,
				nargs="?",
				default=self.default
			)

class Option:
	def __init__(self, name, description, type, default):
		self.name = name
		self.description = description
		self.type = type
		self.default = default
		self.required = default is None

	def define_on(self, parser):
		if self.required:
			parser.add_argument(
				"--" + self.name,
				help=self.description,
				type=self.type
			)
		else:
			parser.add_argument(
				"--" + self.name,
				help=self.description,
				type=self.type,
				nargs="?",
				default=self.default
			)

class Flag:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def define_on(self, parser):
		parser.add_argument(
			"--" + self.name,
			help=self.description,
			action="store_true"
		)
