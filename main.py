import argparse
from scanner.scanner import Scanner
from scanner.payload_manager import PayloadManager

def main():
    parser = argparse.ArgumentParser(description="AI-Driven Vulnerability Scanner")
    parser.add_argument("--url", type=str, required=True, help="Target URL")
    parser.add_argument("--params", type=str, nargs="*", help="URL parameters to target")
    parser.add_argument("--payloads", type=str, help="Path to custom payloads")
    parser.add_argument("--report", type=str, default="reports/scan_report.json", help="Path to save the report")
    args = parser.parse_args()

    payload_manager = PayloadManager(args.payloads or "payloads/")
    scanner = Scanner(args.url, args.params, payload_manager)
    results = scanner.run_scan()

    scanner.save_report(results, args.report)
    print(f"Scan completed! Report saved at: {args.report}")

if __name__ == "__main__":
    main()   
auth = Authentication("https://example.com/login", {"username": "user", "password": "pass"})
if auth.login():
    scanner = Scanner(args.url, args.params, payload_manager, session=auth.get_authenticated_session())
