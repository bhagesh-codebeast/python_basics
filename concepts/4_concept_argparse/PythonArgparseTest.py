from PythonArgparse import ParseParams

# Declare variables for yaml file and description
yamlfile = "PythonArgparse.yaml"
description = "testing argparse"

# Parse yaml file and description to ParseParams class
args = ParseParams(yamlfile, description).args

# access args as attributes
print(args.file, args.file2)

# access specific method
parser = ParseParams(yamlfile, description)
print(parser.ReadYaml())
