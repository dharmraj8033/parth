import httpx
import json

class Scanner:
    def __init__(self, url, parameters, payload_manager):
        self.url = url
        self.parameters = parameters or []
        self.payload_manager = payload_manager

    def run_scan(self):
        results = []
        for payload in self.payload_manager.get_payloads():
            for param in self.parameters:
                modified_url = self.inject_payload(self.url, param, payload)
                response = self.send_request(modified_url)
                if self.detect_vulnerability(response):
                    results.append({
                        "url": modified_url,
                        "parameter": param,
                        "payload": payload,
                        "response": response.text
                    })
        return results

    def inject_payload(self, url, parameter, payload):
        if "?" not in url:
            url += "?"
        return f"{url}&{parameter}={payload}"

    def send_request(self, url):
        try:
            return httpx.get(url, timeout=5)
        except Exception as e:
            return None

    def detect_vulnerability(self, response):
        # Simplified detection logic; extend for real use
        if response and "<script>" in response.text:
            return True
        return False

    def save_report(self, results, path):
        with open(path, "w") as f:
            json.dump(results, f, indent=4)
