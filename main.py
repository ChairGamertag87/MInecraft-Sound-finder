import json
import os
import shutil

with open('indexes/17.json') as data_file:
    data = json.load(data_file)

os.makedirs('extracted/assets')

for f in data["objects"]:
    if not os.path.exists('extracted/assets/' + f.rsplit('/', 1)[0]):
        os.makedirs('extracted/assets/' + f.rsplit('/', 1)[0])
    print(f)
    shutil.copy2('objects/' + data["objects"][f]["hash"][:2] + '/' + data["objects"][f]["hash"], 'extracted/assets/' + f)
