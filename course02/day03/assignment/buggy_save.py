import json

with open("save.json", "w") as f:
    json.dump({"hp": 10}, f)
