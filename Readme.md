Automated Link Checker
This project is a web-based tool that automatically generates and verifies the status of random links for any website. It uses a Python Flask backend to perform the checks and a clean HTML/JavaScript frontend to display the results in real-time.

This tool solves the browser's CORS (Cross-Origin Resource Sharing) security limitations by delegating the URL checking to a server-side script, which can freely access external websites.

Features
Automated Checking: Click one button to generate a batch of 10 random links and automatically check their status.

Real-Time UI Updates: The frontend updates instantly as the backend determines if each link is alive or dead.

Clear Status Tracking: See a live count of alive, dead, and pending links.

Copy Functionality: Easily copy all discovered "alive" links to your clipboard.

Clean & Modern UI: A responsive and easy-to-use interface built with Tailwind CSS.

Configurable: Set the base URL and the string that indicates an inactive link.

Technical Architecture
This project is composed of two main parts:

Frontend (templates/index.html)

A static HTML file that runs in the browser.

It generates the random link codes and displays the UI.

It uses JavaScript's fetch API to send each generated URL to the Python backend for verification.

It is responsible for all visual updates based on the backend's response.

Backend (server.py)

A lightweight web server built with Python and the Flask framework.

It exposes a single API endpoint (/check).

When it receives a URL and an "inactive content string", it uses the requests library to fetch the page's HTML content.

It checks the HTML for the specific inactive string to determine if the link is active.

It sends a simple JSON response ({'status': 'alive'} or {'status': 'dead'}) back to the frontend.

Setup and Installation
Follow these steps to run the project locally. You will need Python 3.6+ installed.

Step 1: Clone the Repository
Clone this project to your local machine.

git clone <your-repository-url>
cd <your-repository-folder>

Step 2: Set Up a Python Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Step 3: Install Dependencies
Install the required Python packages using the requirements.txt file.

pip install -r requirements.txt

Step 4: Verify the Folder Structure
Ensure your project has the correct folder structure. Flask requires HTML files to be in a templates folder by default.

/your-project-folder/
|-- server.py
|-- requirements.txt
|-- README.md
└── templates/
    └── index.html

Step 5: Run the Backend Server
Start the Flask server.

python server.py

You should see output indicating that the server is running on http://127.0.0.1:5000. Keep this terminal window open.

Step 6: Run the Frontend
Open the index.html file (located inside the templates folder) directly in your web browser (e.g., by double-clicking it).

Enter the base URL for the links you want to check (e.g., https://gofile.io/d/) and the text that appears on a page when the content is not available (e.g., "This content does not exist").

You can now use the tool! The frontend running in your browser will communicate with the Python server you started in the previous step.