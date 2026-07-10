#!/usr/bin/env python3
"""Simple Prometheus exporter (works on Windows Docker Desktop too)."""
import random
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

STARTED = time.time()


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        return

    def do_GET(self):
        if self.path != "/metrics":
            self.send_response(404)
            self.end_headers()
            return
        cpu = 20 + random.random() * 40
        mem = 40 + random.random() * 30
        body = f"""# HELP lab_cpu_usage_percent Demo CPU usage
# TYPE lab_cpu_usage_percent gauge
lab_cpu_usage_percent {cpu:.2f}
# HELP lab_memory_usage_percent Demo memory usage
# TYPE lab_memory_usage_percent gauge
lab_memory_usage_percent {mem:.2f}
# HELP lab_up 1 if exporter is up
# TYPE lab_up gauge
lab_up 1
# HELP lab_uptime_seconds Exporter uptime
# TYPE lab_uptime_seconds gauge
lab_uptime_seconds {time.time() - STARTED:.2f}
"""
        data = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 9100), H).serve_forever()
