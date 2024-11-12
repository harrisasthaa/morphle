from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    name = "John Doe"  # Example name
    # System username
    username = os.getenv("USER", os.getenv("USERNAME", "codespace"))  # Example username
    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Running the 'top' command and capturing output
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")

    # Construct the response
    response = f"Name: {name}\nUsername: {username}\nServer Time: {server_time}\nTOP output:\n{top_output}"
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
