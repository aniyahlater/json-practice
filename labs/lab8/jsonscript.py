#!/bin/bash
#simply reading the file 
import json
with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
#going to only parse the first 5 entries 
five = data[:5]
for each in five:
# pulling out the following fields: name, html_url, updated_at, and visibility
    with open("chacon.csv","a") as file:
        csl = each['name'] +  ',' + each['html_url'] + ',' + each['updated_at'] + ',' + each['visibility'] + '\n'
        file.write(csl)


