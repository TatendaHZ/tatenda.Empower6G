import requests

# API configuration
API_ROOT = "http://192.168.3.89:30991/"
BASE_PATH = "qod/v0"

# Read the session ID from the file
session_file = "session_info.txt"
try:
    with open(session_file, "r") as f:
        lines = f.readlines()
        session_id = None
        for line in lines:
            if line.startswith("Session ID:"):
                session_id = line.split(":", 1)[1].strip()
                break

    if not session_id:
        raise ValueError("Session ID not found in the file.")

except FileNotFoundError:
    print(f"File {session_file} not found.")
    exit(1)
except ValueError as ve:
    print(ve)
    exit(1)

# Construct the DELETE endpoint
DELETE_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions/{session_id}"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

try:
    # Send DELETE request to terminate the session
    response = requests.delete(DELETE_ENDPOINT, headers=headers)

    # Check if the request was successful
    if response.status_code == 204:
        print(f"Session {session_id} deleted successfully!")
    else:
        print(f"Failed to delete session. Status code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error occurred while making the request: {e}")
