import json
import sys

def output_to_file_or_stdout(data, output_file):
    if output_file:
        with open(output_file, 'w') as file:
            json.dump(data, file)
    else:
        json.dump(data, sys.stdout)