import requests

# API configuration
API_ROOT = "http://192.168.88.40:30991/"
BASE_PATH = "qod/v0"
SESSION_ID = "d10b0ad0-4997-4642-b57d-85c2f6349b31"  # From the session creation response
DELETE_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions/{SESSION_ID}"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

try:
    # Send DELETE request to terminate the session
    response = requests.delete(DELETE_ENDPOINT, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 204:
        print(f"Session {SESSION_ID} deleted successfully!")
    else:
        print(f"Failed to delete session. Status code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error occurred while making the request: {e}")
