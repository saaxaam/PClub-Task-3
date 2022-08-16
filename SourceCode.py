import requests
import json
from collections import Counter

data = requests.get("https://summerofcode.withgoogle.com/api/program/2022/organizations/").json()
content = []

for i in data:
    c = Counter()
    c["name"] = i["name"]
    c["description"] = i["description"]
    c["tech-stack"] = i["tech_tags"]
    content.append(dict(c))

for i in range(50):
    print(json.dumps(content[i],indent=1))
