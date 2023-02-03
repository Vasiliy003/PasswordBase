import json


data = {"Georgia": "180923"}
with open("sign_base.json", "w") as f:
    json.dump(data, f)

