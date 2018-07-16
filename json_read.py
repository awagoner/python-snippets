import json
import pprint # Pretty Print

dta = []

with open("/files/data/sample.json") as json_file:
    for line in json_file:
        line = json.loads(line)
        dta.append(line)

# pretty print the first json line
pprint(dta[0])
