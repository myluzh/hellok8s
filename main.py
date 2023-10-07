import http.server
import socketserver
import socket
import time
from datetime import datetime

import os

import http.server
import os
import socket
from datetime import datetime


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        db_host = os.environ.get('DB_HOST')
        db_username = os.environ.get('DB_USERNAME')
        db_password = os.environ.get('DB_PASSWORD')
        env_vars = {k: v for k, v in os.environ.items() if not k.startswith("__")}
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Hello, K8S!</title>
                <style>
                    body {{
                        background-color: #f2f2f2;
                        font-family: Arial, Helvetica, sans-serif;
                    }}
                    .container {{
                        padding: 20px;
                        margin: 50px auto;
                        width: 80%;
                        background-color: #fff;
                        border-radius: 10px;
                        -webkit-box-shadow: 0px 0px 15px 0px rgba(0,0,0,0.75);
                        -moz-box-shadow: 0px 0px 15px 0px rgba(0,0,0,0.75);
                        box-shadow: 0px 0px 15px 0px rgba(0,0,0,0.75);
                    }}
                    table {{
                        border-collapse: collapse;
                        width: 100%;
                    }}
                    th, td {{
                        text-align: left;
                        padding: 8px;
                    }}
                    th {{
                        background-color: #0066cc;
                        color: white;
                    }}
                    tr:nth-child(even) {{
                        background-color: #f2f2f2;
                    }}
                    a {{
                        color: #0066cc;
                        text-decoration: none;
                    }}
                    td {{
                        word-wrap: break-word;
                        max-width: 300px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Hello, K8S! <br>Created by myluzh at {timestamp}</h1>
                    <p>Here's some information about the running pod:</p>
                    <table>
                        <tr>
                            <th>Hostname</th>
                            <td>{hostname}</td>
                        </tr>
                        <tr>
                            <th>IP Address</th>
                            <td>{ip_address}</td>
                        </tr>
                        <tr>
                            <th>DB Host</th>
                            <td>{db_host}</td>
                        </tr>
                        <tr>
                            <th>DB Username</th>
                            <td>{db_username}</td>
                        </tr>
                        <tr>
                            <th>DB Password</th>
                            <td>{db_password}</td>
                        </tr>
                    </table>
                    <br>
                    <p>Here are some system environment variables:</p>
                    <table>
                        {"".join(f"<tr><th>{key}</th><td>{value}</td></tr>" for key, value in env_vars.items())}
                    </table>
                    <br>
                    <p>Created by myluzh at {timestamp}</p>
                </div>
            </body>
        </html>
        """

        self.wfile.write(html.encode())

PORT = 80

import logging

# 设置日志级别为INFO
logging.basicConfig(level=logging.INFO)




while True:
    logging.info("run hello k8s")
    try:
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            import os
            # 开始
            logging.info(f"Serving at http://localhost:{PORT}")
            httpd.serve_forever()
    except Exception as e:
        logging.info(e)
        time.sleep(3)
        pass


