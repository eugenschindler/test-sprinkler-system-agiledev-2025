# view_log.py

import json

class ViewLog:
    def generate_html_report(self, log_file="system_log.json"):
        with open(log_file, "r") as file:
            logs = file.readlines()
        
        html = "<html><head><title>Sprinkler System Log</title></head><body>"
        html += "<h1>Sprinkler System Log</h1>"
        html += "<table border='1'><tr><th>Settings</th><th>Sensor Data</th><th>Actions</th></tr>"

        for log in logs:
            log_entry = json.loads(log)
            html += f"<tr><td>{log_entry['settings']}</td><td>{log_entry['sensor_data']}</td><td>{log_entry['actions']}</td></tr>"

        html += "</table></body></html>"
        with open("log_report.html", "w") as report_file:
            report_file.write(html)
        print("HTML report generated.")
