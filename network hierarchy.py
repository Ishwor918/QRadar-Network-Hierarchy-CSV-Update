import csv
import json

json_data = []

with open(r'C:\Users\<user>\Desktop\network hierarchy.csv',"r") as f: ##replace with file path
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        network_hierarchy = {
             "group" : row[0],
             "name" : row[1],
             "cidr" : row[2],
             "description" : row[3],
             "domian" : row[1]
        }
        json_data.append(network_hierarchy)

with open(r'C:\Users\<user>\Desktop\data.json',"w") as f: ##replace with json output file path
        json.dump(json_data, f, indent=1)
