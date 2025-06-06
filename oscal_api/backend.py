import os
import json
import glob

DEFAULT_ROOT_DIR = "./files"

class FileBackend:

    def __init__(self, rootdir: str = DEFAULT_ROOT_DIR):
        self.rootdir = rootdir

    def find_all(self, model: str):
        query = os.path.join(self.rootdir, model, "*.json")
        files = glob.glob(query)

        items = []
        for file in files:
            with open(file, 'r') as f:
                data = json.load(f)
                items.append({
                    "uuid": data[model]["uuid"],
                    "metadata": data[model]["metadata"]
                })
        return items

    def find_one(self, model: str, uuid: str):
        query = os.path.join(self.rootdir, model, "*.json")
        files = glob.glob(query)
        for file in files:
            with open(file, 'r') as f:
                data = json.load(f)
                if data[model]["uuid"] == uuid:
                    return data[model]

    def create_one(self, model: str, data: dict):
        filename = f"{data[model]['uuid']}.json"
        filepath = os.path.join(self.rootdir, model, filename)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4) 

    def update_one(self, uuid):
        pass

    def delete_one(self, subdir, uuid):
        pass
