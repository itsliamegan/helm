from setuptools import setup, find_packages

setup(
	name="helm",
	version="0.1.0",
	packages=find_packages(include=["helm", "helm.*"]),
	install_requires=[
	],
	extras_require={
		"dev": [
			"pytest"
		]
	}
)
