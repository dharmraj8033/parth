import json

class ReportGenerator:
    def save_as_json(self, results, path):
        with open(path, "w") as f:
            json.dump(results, f, indent=4)
