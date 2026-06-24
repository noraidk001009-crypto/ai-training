import json
f = open("save.json", "w")
json.dump({"hp": 10}, f)
# forgot to close — rewrite with with open
