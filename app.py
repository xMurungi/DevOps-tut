# app.py
from flask import Flask, jsonify
import platform
import socket

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/')
def get_devops_info():
    """
    This function is the core of our API.
    It gathers system info and returns it as JSON.
    """
    try:
        # Get the hostname of the machine
        hostname = socket.gethostname()
        # Get the IP address associated with the hostname
        ip_address = socket.gethostbyname(hostname)
    except Exception as e:
        hostname = "N/A"
        ip_address = f"Could not resolve: {e}"

    # Create a dictionary (a key-value structure) to hold our data
    info = {
        "message": "Hello from the DevOps Info API!",
        "systemInfo": {
            "hostname": hostname,
            "ipAddress": ip_address,
            "platform": platform.system(),       # e.g., 'Linux', 'Windows', 'Darwin'
            "platformRelease": platform.release(), # e.g., Kernel version
            "architecture": platform.machine()     # e.g., 'x86_64'
        },
        "createdBy": "Joses Murungi"
    }

    # Use jsonify to convert our dictionary to a proper JSON response
    return jsonify(info)

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible from outside the container
    # Use port 8080, a common alternative to 5000
    app.run(host='0.0.0.0', port=8080)

