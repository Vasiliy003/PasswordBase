import json
from hashlib import sha256



password = sha256()
data = {"Georgia": "180923"}
with open("sign_base.json", "w") as f:
    json.dump(data, f)

