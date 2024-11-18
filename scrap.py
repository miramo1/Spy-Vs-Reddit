import os
import pandas as pd
import json
from aliasFunctions import values_as_keys

# folder_path = r"C:\Users\pinkm\Desktop\stock_data"
# to_remove = [i.strip() for i in open("text.txt")]

# for item in to_remove:
#     pathing = f"{folder_path}/{item}"
#     if os.path.exists(pathing):
#         print(pathing)
#         # os.remove(pathing)

# values_as_keys("alias.json")
# omit = [i.strip() for i in open("text.txt")]
# with_tag = ["$"+item for item in omit]
# omit.extend(with_tag) 

# data = json.load(open("alias.json"))
# empty = {}

# for k, v in data.items():
#     if k in omit or v in omit:
#         continue
#     else:
#         empty[k] = v

# with open("json_file2", "w") as f:
#     f.write(json.dumps(empty, indent=4))