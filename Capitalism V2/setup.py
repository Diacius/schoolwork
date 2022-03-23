import json
list = ["potato","tomato","beer","egg"]
with open("list", "w") as fp:
    json.dump(list, fp)
