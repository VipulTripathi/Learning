import json
from jsonFiles.data import data

person='{"name": "Bob", "languages": ["English", "Fench"]}'
persondict=json.loads(person)

for i in data:
    print(i,data[i])
