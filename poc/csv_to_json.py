import json
import pandas as pd

nodes = pd.read_csv("nodes.csv", sep="|") 
links = pd.read_csv("links.csv", sep="|")
nodes["name"] = nodes.apply(lambda x: json.loads(x["fields"]).get("name"),axis=1)
nodes["url"] = nodes.apply(lambda x: json.loads(x["fields"]).get("url"),axis=1)
nodes["address"] = nodes.apply(lambda x: json.loads(x["fields"]).get("address"),axis=1)
nodes = nodes.drop("fields", axis=1)
graph = {
    "nodes": json.loads(nodes.to_json(orient='records')),
    "links": json.loads(links.to_json(orient='records'))
}
with open("data.json", "w") as i:
    json.dump(graph, i)