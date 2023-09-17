import argparse
import yaml

# Python Class to read yaml file and parse command line arguments
class ParseParams:
	def __init__(self, yaml_file, description):
		self.yaml_file = yaml_file
		self.description = description
		self.yaml_dict = self.ReadYaml()
		self.args = self.ParseArgs()
	# Method to read yaml file and store in dictionary
	def ReadYaml(self):
		with open(self.yaml_file, "r") as yaml_file:
			yaml_dict = yaml.safe_load(yaml_file)
		return yaml_dict
	# Method to read command line arguments
	def ParseArgs(self):
		parser = argparse.ArgumentParser(self.description)
		for arguments in self.yaml_dict:
			parser.add_argument(self.yaml_dict[arguments]["flag"], self.yaml_dict[arguments]["name"], help=self.yaml_dict[arguments]["help"], default=self.yaml_dict[arguments]["default"], required=self.yaml_dict[arguments]["required"])
		args = parser.parse_args()
		return args

if __name__ == "__main__":
	example_file = "PythonArgparse.yaml"
	example_description = "testing argparse"

	arguments = ParseParams(example_file,example_description)
	
	print(arguments.args)