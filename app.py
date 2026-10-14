
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud PaaS Web Application</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef2f7;
                text-align: center;
                padding: 60px 20px;
            }
            .card {
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 35px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #00000015;
            }
            h1 { color: #2457a7; }
            p { color: #444; line-height: 1.7; }
            .status {
                display: inline-block;
                background: #e0f7e9;
                color: #16713b;
                padding: 10px 16px;
                border-radius: 20px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Cloud PaaS Web Application</h1>
            <p>Welcome to my Cloud Computing Lab Practical 5.</p>
            <p>This web application is developed using Python and Flask.</p>
            <p>It is deployed using Platform as a Service (PaaS).</p>
            <div class="status">Application is running!</div>
        </div>
    </body>
    </html>
    """

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
   
