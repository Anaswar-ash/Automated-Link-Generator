# File: server.py
# Description: A Flask backend to check the status of URLs and serve the frontend.

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

# Initialize Flask app
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) to allow the frontend to communicate with this server
CORS(app)

@app.route('/')
def index():
    """Serves the main index.html page."""
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_url_status():
    """
    Receives a URL and an inactive string, fetches the URL's content, 
    and checks for the inactive string.
    Returns 'alive' or 'dead'.
    """
    data = request.get_json()
    url_to_check = data.get('url')
    inactive_string = data.get('inactive_string')

    if not url_to_check or not inactive_string:
        return jsonify({'status': 'error', 'message': 'URL or inactive string not provided'}), 400

    try:
        # Send a GET request to the URL with a timeout
        response = requests.get(url_to_check, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Check if the specific error text is present in the page's HTML content
        if inactive_string in response.text:
            return jsonify({'status': 'dead'})
        else:
            return jsonify({'status': 'alive'})

    except requests.exceptions.RequestException as e:
        # Handle network errors, timeouts, or bad status codes
        print(f"Error checking {url_to_check}: {e}")
        return jsonify({'status': 'error', 'message': f'Failed to fetch URL: {e}'})

if __name__ == '__main__':
    # Run the server on port 5000 in debug mode
    print("Starting the link checker server.")
    print("Access the application at: http://127.0.0.1:5000")
    app.run(port=5000, debug=True)

