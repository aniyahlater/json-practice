#!/bin/bash
#simply reading the file 
import json
with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
# pulling out the following fields: name, html_url, updated_at, and visibility
#import requests
#response=requests.get(data)
#response.
print(data)
