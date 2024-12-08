from flask import Flask, request, render_template, jsonify
from scanner.scanner import Scanner
from scanner.payload_manager import PayloadManager
import plotly.express as px

@app.route('/dashboard')
def dashboard():
    # Mock data for demonstration
    data = {"Vulnerabilities": ["XSS", "SQLi", "Command Injection"], "Count": [5, 2, 1]}
    fig = px.bar(data, x="Vulnerabilities", y="Count", title="Scan Results")
    graph_html = fig.to_html(full_html=False)
    return render_template("dashboard.html", graph_html=graph_html)

app = Flask(__name__)
payload_manager = PayloadManager("payloads/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data['url']
    params = data.get('params', [])
    payloads = data.get('payloads', [])

    scanner = Scanner(url, params, payload_manager)
    results = scanner.run_scan()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
