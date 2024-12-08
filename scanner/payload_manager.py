import os

class PayloadManager:
    def __init__(self, payload_dir):
        self.payload_dir = payload_dir

    def get_payloads(self):
        payloads = []
        for file in os.listdir(self.payload_dir):
            with open(os.path.join(self.payload_dir, file), "r") as f:
                payloads.extend(f.read().splitlines())
        return payloads
